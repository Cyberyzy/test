---
title: Elliptic Function
publishDate: 2023-05-02 19:59:45
description: 'Introduction of elliptic function~💩'
tags:
  - Elliptic Function
language: 'English'
---
<!--more-->

## Approach from Jacobi

Jacobi considered the exact solution of Motion of Simple Pendulum. Let $ m $ be the mass of the
bob at the end of the pendulum, $ a $ be the length of the pendulum, $ \theta $ be the
angle of inclination which the pendulum makes with a vertical line,$ \alpha $ be the
initial angle of inclination when the pendulum is released from rest position
at time zero, $ t $ be the time variable, and $ g  $ be the constant of the gravity of
the earth. The equation of the conservation of energy is $$
    \frac{1}{2}ma^2\left(\frac{d\theta}{dt}\right)-mgacos\theta=-mgacos\alpha
$$

Replace $ cos\theta $ by $ 1-\dfrac{\theta^2}{2} $ to give $$
    \left(\frac{d\theta}{dt}\right)^2+A\theta^2=B
$$  
solution is $$
    t=\rho sin(\sigma \theta+\tau)
$$

But what is the exact solution?

Exchange function by using double angle formula
$$
     \left(\frac{d\theta}{dt}\right)^2=2\frac{g}{a}(cos\theta-cos\alpha)=4\frac{g}{a}(sin^2\dfrac{\alpha}{2}-sin^2\dfrac{\theta}{2})
$$
$$
    =4\frac{gsin^2\frac{\alpha}{2}}{a}(1-\left(\frac{sin\frac{\theta}{2}}{sin\frac{\alpha}{2}}\right)^2)
$$

What does it mean?

$$
    cos\theta\approx 1-\frac{\theta^2}{2}\space and\space cos\theta=1-2sin^2(\theta)
$$
gives out the motivation. Exchange $ sin\frac{\alpha}{2} $ as $ sin\varphi $, then$$
    \left(\dfrac{d\varphi}{dt}\right)^2=\dfrac{g}{a}\left(1-\sin^2\dfrac{\alpha}{2}\sin^2\varphi\right).
$$
and the solution is$$
    t=\sqrt{\dfrac{a}{g}}\int_{\psi=0}^{\varphi}\dfrac{d\psi}{\sqrt{1-\sin^2\frac{\alpha}{2}\sin^2\psi}}.
$$
We also know $$
    \int_{0}^{\frac{\pi}{2}}\sin^{2n}\varphi d\varphi=\dfrac{\pi}{2}\cdot\dfrac{1\cdot3\cdot5\cdots(2n-1)}{2\cdot4\cdot6\cdots(2n)}
$$
by residue theorem, we can take Taylor expansion of the solution which is $$
    \begin{gathered}
=2\pi\sqrt{\frac{a}{g}}\left(1+\left(\frac{1}{2}\right)^{2}k^{2}+\left(\frac{1\cdot3}{2\cdot4}\right)^{2}k^{4}+\cdots\right)
\end{gathered}
$$

That is where elliptic function araises

We call integrals like
$$
    I=\int_{z_1}^{z}\frac{dz}{\sqrt{(1-z^2)(1-k^2z^2)}}
$$
as **Jacobi Elliptic Function**.

## Abel's approach

Consider the integration of the 1-form$$
    \omega:=\frac{dz}{\sqrt{(1-z^2)(1-k^2z^2)}},\quad z\in \mathbb{C}
$$
function$$
    \sqrt{(1-z^2)(1-k^2z^2)}
$$
has four roots and it's double-valued. We want to turn it into single-valued. The idea is construct a **new structure** replace a single point by two points(except $ z=\pm 1,\pm 1/k $ )

on the domain obtained by removing the two branch-cuts [−1/k,−1] and [1,1/k]
from the Riemann sphere $ \mathbb{P}_1 =\mathbb{C} \bigcup \{\infty\}  $ . The two branches are the negative of each other. Any of the two branches take values of opposite sign on both edges of each of the two branch-cuts. To get the Riemann surface X we can take two copies of $ \mathbb{P}_1-\left(\left[\frac{-1}{k},-1\right]\cup\left[1,\frac{1}{k}\right]\right) $ and join them by identifying the upper
edge of $ \left[\frac{-1}{k},-1\right] $  in one copy identified with the lower edge of $ \left[\frac{-1}{k},-1\right] $
in the
other copy and at the same time identifying the upper edge of $ \left[1,\frac{1}{k}\right] $
in onecopy identified with the lower edge of $ \left[1,\frac{1}{k}\right] $ in the other copy.

## Weierstrass $ \wp(z) $ function

We all know the three fundamental properties of $\wp(z)$

- The sum of the residues of the function inside a fundamental parallelogram is zero.
- The number of zeroes of the function equals the number of poles inside a fundamental parallelogram.
- Inside a fundamental parallelogram the sum of the coordinates of the zeroes equals the sum of the coordinates of the poles modulo a period.

Which can be proved through Argument Principle and Residue Theorem.

Now we want to know some other properties of $ \wp $

### 1. Convergence

Consider $$
    \wp(z)=\frac{1}{z^2}+\sum_{(n_1,n_2)\in\mathbb{Z}^2-(0,0)}\left(\frac{1}{(z-(n_1\omega_1+n_2\omega_2))^2}-\frac{1}{(n_1\omega_1+n_2\omega_2)^2}\right)
$$
Its convergence can be argued by considering the infinite sum as the limit of
the sequence of partial sums
$$
    \sum_{\ell\in L,|\ell|\leq p}\left(\frac{1}{(z-\ell)^2}-\frac{1}{\ell^2}\right)
$$
as $ p \to \infty $  and using the Cauchy criterion for the convergence of a sequence
as follows. The difference between the q-th and the p-th partial sums
$$
    \sum_{\begin{array}{c}\ell\in L,\\ p\leq|\ell|\leq q\end{array}}\left(\frac{1}{(z-\ell)^2}-\frac{1}{\ell^2}\right)
$$
is comparable to
$$
    \sum\limits_{k=p}^q\left(\sum\limits_{k-1\leq|\ell|\leq k+1}\frac{1}{|\ell|^3}\right)\sim\sum\limits_{k=p}^q k\frac{1}{k^3}=\sum\limits_{k=p}^q\frac{1}{k^2}
$$
which goes to 0.

### 2. Taylor Expansion

$$
    \begin{gathered}
F(z) =\frac{1}{z^2}+3s_4z^2+5s_6z^4+\cdots, \\
F'(z) =-\frac2{z^3}+6s_4z+20s_6z^3+\cdots, \\
F'(z)^2 =\frac4{z^6}-\frac{24s_4}{z^2}-80s_6+\cdots, \\
F(z)^3 =\frac{1}{z^6}+\frac{9s_4}{z^2}+15s_6+\cdots
\end{gathered}
$$

### Solution to Stein Complex Analysis Chapter 9💩

##### Exercise 4

By rearranging the series
$$
    \frac{1}{z^2}+\sum\limits_{\omega\in\Lambda^*}\left[\frac{1}{(z+\omega)^2}-\frac{1}{\omega^2}\right]
$$
show directly, without differentiation, that$  \wp(z + \omega) = \wp(z) $  whenever $ \omega\in \Lambda $ .

##### Solution

First we show
$$
\begin{align*}
\wp(z)&=\wp^R(z)+O(\frac{1}{R})\\
&=z^{-2}+\sum_{0<|\omega|< R}((z+\omega) ^{-2}-\omega^{-2})+O(\frac{1}{R})
\end{align*}
$$
Actually, $$
    \begin{align*}
\wp(z)=z^{-2}&+\sum_{0<|\omega|< R}((z+\omega) ^{-2}-\omega^{-2})\\
&+\sum_{|\omega|> R}((z+\omega) ^{-2}-\omega^{-2})
\end{align*}
$$
where $ |z|<\sqrt{R} $.
Then$$
    \left|((z+\omega) ^{-2}-\omega^{-2})\right|=|\frac{2z\omega+z^2}{\omega^2(z-\omega)^2}|<C\frac{1}{|\omega|^3}
$$
When $ R\to \infty $, the summention can be estimated by integration$$
    \sum_{|\omega|> R}((z+\omega) ^{-2}-\omega^{-2})<\sum_{n=R}^{+\infty}\sum_{n-1<|\omega|<n+1}\frac{C}{|\omega|^3}=O( \frac{1}{R})
$$
A fact is used that is $ {n − 1 ≤ |y| ≤
n + 1} $ is almost $ kn $  where $ k $  is a constant. So $ \wp(z)=\wp^R(z)+O(\frac{1}{R}) $

Then, to show $ \wp^R(z+1)-\wp^R(z) $ is $ O(\sum_{R-c<|\omega|<R+c}|\omega|^{-2})=O(\dfrac{1}{R}) $
still use the fact:
$$
    |\wp^R(z+1)-\wp^R(z)|<C+\sum_{R-1\leq|\omega|\leq R+1}\frac{1}{|(z+\omega)^{2}|}\sim O(\frac{1}{R})
$$
where $ |z|<\sqrt{R} $.similarly we can prove it for $ \wp^R(z+\tau)-\wp^R(z)  $

Finally, let$ R\to \infty $, we get the conclusion

##### Exercise 20

Other examples of elliptic integrals providing conformal maps from the upper
half-plane to rectangles are given below
(a)The function
$$
    \int_0^z\frac{d\zeta}{\sqrt{\zeta(\zeta-1)(\zeta-\lambda)}},\quad\text{with}\lambda\in\mathbb{R}\text{and}\lambda\neq1
$$
maps the upper half-plane conformally to a rectangle, one of whose vertices
is the image of the point at infinity.

(b) In the case $ \lambda = −1 $ , the image of
$$
    F(z)=\int_0^z \frac{d\zeta}{\sqrt{\zeta(\zeta^2-1)}}
$$
is a square whose side lengths are $ \frac{\Gamma^2(1/4)}{2\sqrt{2\pi}} $

##### Solution

(a) by applying Prop. 4.1 from the chapter, which tells you about the vertices and angles of the polygon that's mapped to by the real axis.

(b)The image of $ F(z) $ is a rectangle and has four vertices $ F(1),F(\infty),F(0),F(-1) $

If
$$
    |F(1)-F(0)|=|F(\infty)-F(1)|
$$
then it's a square.

Note
$$
\begin{aligned}
F(1)-F(0) &=\int_0^1\frac{d\zeta}{\sqrt{\zeta(\zeta^2-1)}}=\frac1i\int_0^1\frac{d\zeta}{\sqrt{\zeta(1-\zeta^2)}}\\
F(\infty)-F(1) &=\int_1^\infty\frac{d\zeta}{\sqrt{\zeta(\zeta^2-1)}}=\int_0^1\frac{dt}{\sqrt{t(1-t^2)}}\quad(t=1/\zeta)\\
\end{aligned}
$$
So each side of the rectangle is the same length, which means it's a square.
And then
$$
    \begin{aligned}\int_0^1\frac{dt}{\sqrt{t(1-t^2)}}=\int_0^{\frac{\pi}{2}}\frac{d\theta}{\sqrt{\sin\theta}}=\frac{1}{2}\text{B}\left(\frac{1}{2},\frac{1}{4}\right),\end{aligned}
$$
where
$$
    B(\alpha,\beta)=\int_0^1t^{\alpha-1}(1-t)^{\beta-1}dt=\frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}
$$
We will use $ \Gamma(z)\Gamma\left(z+\frac{1}{2}\right)=2^{1-2z}\sqrt{\pi}\Gamma(2z) $ to derive the result.
