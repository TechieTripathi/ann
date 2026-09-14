#!/usr/bin/env python3
"""
Authoritative source for every number in Lecture 2 (Backpropagation).

Run:  python3 scripts/verify-numbers.py
      python3 scripts/verify-numbers.py --torch   (also cross-check with autograd)

Network: 2-2-2, sigmoid everywhere, MSE loss, eta = 0.5.

    L = 1/2 [ (o1 - t1)^2 + (o2 - t2)^2 ]

The 1/2 is deliberate: it cancels the 2 from differentiating the square, so
dL/do = o - t.  Because the output activation is a sigmoid, the blame at an
output neuron keeps BOTH factors:

    dL/dz = (o - t) * o(1 - o)

There is NO cancellation here. That simplification (dL/dz = o - t) belongs to
sigmoid + binary cross-entropy, and is deliberately not used.

Weights, inputs, targets and loss now all follow the canonical Matt Mazur
walkthrough, so every WEIGHT gradient here matches his published numbers
exactly. One deliberate difference: Mazur holds the biases fixed, while we
update them (they are parameters like any other). That does not change any
weight gradient, but it does change the loss after one step:
    Mazur (weights only)      L = 0.291027924
    ours  (weights + biases)  L = 0.280471447
Both are printed below.

If any slide figure disagrees with this script, the SLIDE is wrong.
"""
from math import exp
import sys

def s(z): return 1.0 / (1.0 + exp(-z))

I1, I2 = 0.05, 0.10
T1, T2 = 0.01, 0.99
ETA = 0.5
W0 = dict(w1=0.15, w2=0.20, w3=0.25, w4=0.30, w5=0.40, w6=0.45, w7=0.50, w8=0.55)
B0 = dict(b1a=0.35, b1b=0.35, b2a=0.60, b2b=0.60)


def forward(W, B):
    net_h1 = W['w1']*I1 + W['w2']*I2 + B['b1a']; out_h1 = s(net_h1)
    net_h2 = W['w3']*I1 + W['w4']*I2 + B['b1b']; out_h2 = s(net_h2)
    net_o1 = W['w5']*out_h1 + W['w6']*out_h2 + B['b2a']; out_o1 = s(net_o1)
    net_o2 = W['w7']*out_h1 + W['w8']*out_h2 + B['b2b']; out_o2 = s(net_o2)
    return net_h1, out_h1, net_h2, out_h2, net_o1, out_o1, net_o2, out_o2


def loss(o1, o2):
    return 0.5*((o1-T1)**2 + (o2-T2)**2)


def backward(W, B):
    nh1, oh1, nh2, oh2, no1, oo1, no2, oo2 = forward(W, B)
    # output layer: two factors, no cancellation
    e1, e2 = oo1 - T1, oo2 - T2                 # dL/do
    r1, r2 = oo1*(1-oo1), oo2*(1-oo2)           # do/dz
    d_o1, d_o2 = e1*r1, e2*r2                   # dL/dz
    dL_doh1 = d_o1*W['w5'] + d_o2*W['w7']
    dL_doh2 = d_o1*W['w6'] + d_o2*W['w8']
    d_h1 = dL_doh1 * oh1*(1-oh1)
    d_h2 = dL_doh2 * oh2*(1-oh2)
    g = dict(w1=d_h1*I1, w2=d_h1*I2, w3=d_h2*I1, w4=d_h2*I2,
             w5=d_o1*oh1, w6=d_o1*oh2, w7=d_o2*oh1, w8=d_o2*oh2)
    gb = dict(b1a=d_h1, b1b=d_h2, b2a=d_o1, b2b=d_o2)
    return dict(e1=e1, e2=e2, r1=r1, r2=r2, d_o1=d_o1, d_o2=d_o2,
                dL_doh1=dL_doh1, dL_doh2=dL_doh2, d_h1=d_h1, d_h2=d_h2, g=g, gb=gb)


def step(W, B):
    r = backward(W, B)
    return ({k: v - ETA*r['g'][k] for k, v in W.items()},
            {k: v - ETA*r['gb'][k] for k, v in B.items()})


def main():
    nh1, oh1, nh2, oh2, no1, oo1, no2, oo2 = forward(W0, B0)
    r = backward(W0, B0)
    L0 = loss(oo1, oo2)          # captured before the ladder loop rebinds oo1/oo2

    print("=" * 66)
    print("SLIDES 16-18  forward pass  (unchanged - the loss does not affect it)")
    print("=" * 66)
    print(f"  net_h1 = {nh1:.6f}   out_h1 = {oh1:.9f}")
    print(f"  net_h2 = {nh2:.6f}   out_h2 = {oh2:.9f}")
    print(f"  net_o1 = {no1:.6f}   out_o1 = {oo1:.9f}")
    print(f"  net_o2 = {no2:.6f}   out_o2 = {oo2:.9f}")

    print("\n" + "=" * 66)
    print("SLIDE 18  MSE loss")
    print("=" * 66)
    print(f"  L = 1/2 [ (o1-t1)^2 + (o2-t2)^2 ]")
    print(f"    = 1/2 [ ({oo1-T1:.9f})^2 + ({oo2-T2:.9f})^2 ]")
    print(f"  per-output: {0.5*(oo1-T1)**2:.9f}  +  {0.5*(oo2-T2)**2:.9f}")
    print(f"  L_total = {loss(oo1, oo2):.9f}")
    rounded = 0.5*((0.7514-T1)**2 + (0.7729-T2)**2)
    print(f"  NOTE  computed from UNROUNDED outputs. Using the 4dp display")
    print(f"        values would give {rounded:.9f} - do not quote that.")

    print("\n" + "=" * 66)
    print("SLIDE 19  blame at the output - TWO factors, no cancellation")
    print("=" * 66)
    print(f"  dL/do1   = o1 - t1        = {r['e1']:+.9f}    <- how wrong")
    print(f"  do1/dz   = o1(1-o1)       = {r['r1']:.9f}     <- how responsive")
    print(f"  delta_o1 = dL/dz          = {r['e1']:.6f} x {r['r1']:.6f} = {r['d_o1']:+.9f}")
    print(f"  delta_o2                  = {r['e2']:.6f} x {r['r2']:.6f} = {r['d_o2']:+.9f}")

    print("\n" + "=" * 66)
    print("SLIDE 20  output-layer gradients, and the bias gift")
    print("=" * 66)
    for k in ('w5', 'w6', 'w7', 'w8'):
        print(f"  dL/d{k} = {r['g'][k]:+.9f}   {k}: {W0[k]:.2f} -> {W0[k]-ETA*r['g'][k]:.9f}")
    print(f"  dL/db2 = [{r['gb']['b2a']:+.9f}, {r['gb']['b2b']:+.9f}]   (= delta, exactly)")

    print("\n" + "=" * 66)
    print("SLIDE 21  a hidden neuron is blamed by everyone it feeds")
    print("=" * 66)
    p1, p2 = r['d_o1']*W0['w5'], r['d_o2']*W0['w7']
    print(f"  via o1: {r['d_o1']:+.9f} x {W0['w5']:.2f} = {p1:+.9f}")
    print(f"  via o2: {r['d_o2']:+.9f} x {W0['w7']:.2f} = {p2:+.9f}   <- OPPOSITE SIGN")
    print(f"  dL/dout_h1 = {r['dL_doh1']:+.9f}")
    print(f"  delta_h1   = {r['dL_doh1']:+.9f} x {oh1*(1-oh1):.9f} = {r['d_h1']:+.9f}")
    print(f"  delta_h2   = {r['d_h2']:+.9f}")

    print("\n" + "=" * 66)
    print("SLIDE 22  all gradients, one simultaneous step")
    print("=" * 66)
    for k in ('w1', 'w2', 'w3', 'w4'):
        print(f"  dL/d{k} = {r['g'][k]:+.9f}   {k}: {W0[k]:.2f} -> {W0[k]-ETA*r['g'][k]:.9f}")
    print(f"  dL/db1 = [{r['gb']['b1a']:+.9f}, {r['gb']['b1b']:+.9f}]")
    print(f"  b1: [0.35, 0.35] -> [{B0['b1a']-ETA*r['gb']['b1a']:.9f}, {B0['b1b']-ETA*r['gb']['b1b']:.9f}]")
    print(f"  b2: [0.60, 0.60] -> [{B0['b2a']-ETA*r['gb']['b2a']:.9f}, {B0['b2b']-ETA*r['gb']['b2b']:.9f}]")
    print("\n  MUST-SAY  the minus sign does not mean 'decrease':")
    for k in ('w5', 'w7'):
        d = 'DOWN' if r['g'][k] > 0 else 'UP'
        print(f"    {k}: grad {r['g'][k]:+.9f}  ->  {W0[k]:.2f} -> {W0[k]-ETA*r['g'][k]:.4f}  ({d})")
    print("  and the two output biases, which start equal, diverge:")
    print(f"    b2: [0.60, 0.60] -> [{B0['b2a']-ETA*r['gb']['b2a']:.4f}, {B0['b2b']-ETA*r['gb']['b2b']:.4f}]")

    # one step, with and without updating the biases (Mazur holds them fixed)
    Wn = {k: v - ETA*r['g'][k] for k, v in W0.items()}
    Bn = {k: v - ETA*r['gb'][k] for k, v in B0.items()}
    *_, q1, _, q2 = forward(Wn, B0)          # weights only, biases frozen
    *_, p1, _, p2 = forward(Wn, Bn)          # weights AND biases
    print("\n  after ONE step:")
    print(f"    weights only  (Mazur's convention) L = {loss(q1, q2):.9f}")
    print(f"    weights + biases (ours)            L = {loss(p1, p2):.9f}")

    print("\n" + "=" * 66)
    print("SLIDE 22  convergence ladder")
    print("=" * 66)
    W, B = dict(W0), dict(B0)
    marks = {0, 1, 2, 10, 100, 1000, 10000}
    for n in range(10001):
        *_, oo1, _, oo2 = forward(W, B)
        if n in marks:
            print(f"  {n:>6} steps   L = {loss(oo1, oo2):.8f}   out = [{oo1:.4f}, {oo2:.4f}]")
        W, B = step(W, B)

    print("\n" + "=" * 66)
    print("SLIDES 25-26  vanishing gradients, and what MSE costs us")
    print("=" * 66)
    print(f"  max sigma'(z) = 0.25")
    for n in (2, 5, 10, 20):
        print(f"    {n:>2} sigmoid layers: 0.25^{n} = {0.25**n:.3e}")
    print("  ReLU: sigma' = 1 for z>0  ->  1^n = 1 at any depth")
    print(f"\n  On THIS forward pass, delta at o1 under each loss:")
    print(f"    MSE           (o-t) o(1-o) = {r['d_o1']:.9f}")
    print(f"    cross-entropy (o-t)        = {r['e1']:.9f}   {r['e1']/r['d_o1']:.2f}x larger")
    o = 0.999
    print(f"\n  Confidently wrong: predict {o}, truth 0")
    print(f"    MSE           dL/dz = (o-t)o(1-o) = {(o-0)*o*(1-o):.9f}   <- barely learns")
    print(f"    cross-entropy dL/dz = (o-t)       = {o-0:.9f}")
    print(f"    ratio = {1/(o*(1-o)):.1f}x")

    if '--torch' in sys.argv:
        cross_check(r, L0)


def cross_check(r, L_total):
    try:
        import torch
    except ImportError:
        print("\n[--torch] PyTorch not installed; skipping autograd cross-check.")
        return
    print("\n" + "=" * 66)
    print("AUTOGRAD CROSS-CHECK  (float64)")
    print("=" * 66)
    x = torch.tensor([I1, I2], dtype=torch.float64)
    y = torch.tensor([T1, T2], dtype=torch.float64)
    W1 = torch.tensor([[W0['w1'], W0['w2']], [W0['w3'], W0['w4']]], dtype=torch.float64, requires_grad=True)
    b1 = torch.tensor([B0['b1a'], B0['b1b']], dtype=torch.float64, requires_grad=True)
    W2 = torch.tensor([[W0['w5'], W0['w6']], [W0['w7'], W0['w8']]], dtype=torch.float64, requires_grad=True)
    b2 = torch.tensor([B0['b2a'], B0['b2b']], dtype=torch.float64, requires_grad=True)
    h = torch.sigmoid(W1 @ x + b1)
    yh = torch.sigmoid(W2 @ h + b2)
    lo = 0.5 * ((yh - y) ** 2).sum()
    lo.backward()
    checks = [("L_total", L_total, lo.item()),
              ("dL/dw5", r['g']['w5'], W2.grad[0, 0].item()),
              ("dL/dw6", r['g']['w6'], W2.grad[0, 1].item()),
              ("dL/dw7", r['g']['w7'], W2.grad[1, 0].item()),
              ("dL/dw8", r['g']['w8'], W2.grad[1, 1].item()),
              ("dL/dw1", r['g']['w1'], W1.grad[0, 0].item()),
              ("dL/dw2", r['g']['w2'], W1.grad[0, 1].item()),
              ("dL/dw3", r['g']['w3'], W1.grad[1, 0].item()),
              ("dL/dw4", r['g']['w4'], W1.grad[1, 1].item()),
              ("dL/db1a", r['gb']['b1a'], b1.grad[0].item()),
              ("dL/db1b", r['gb']['b1b'], b1.grad[1].item()),
              ("dL/db2a", r['gb']['b2a'], b2.grad[0].item()),
              ("dL/db2b", r['gb']['b2b'], b2.grad[1].item())]
    ok = True
    for name, hand, t in checks:
        m = abs(hand - t) < 5e-9
        ok &= m
        print(f"  {name:<9} hand {hand: .9f}   torch {t: .9f}   {'OK' if m else 'MISMATCH'}")
    print("\n  ALL MATCH" if ok else "\n  *** MISMATCH - DO NOT SHIP ***")


if __name__ == '__main__':
    main()
