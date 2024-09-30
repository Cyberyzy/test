---
title: Montel Theorem
publishDate: 2023-05-25 19:54:16
description: 'Introduction to Montel Theorem'
tags:
  - Complex Analysis
  - Montel Theorem
language: 'English'
---

A function family $ \mathcal{F} $ is called **normal** if every sequence of function $ \{f_n\}\in \mathcal{F} $ is uniformly convergent in every compact subset of $ \Omega $. The limit of $ \{f_n\} $ does not need to be a member of $ \mathcal{F} $. If the limit is $ \infty $, it does not matter.

In order to verify a function family is normal, we actually have methods below:

## Montel Theorem

Montel Theorem tells us that a locally bounded function family is normal.

If the family $ \mathcal{F} $ is uniformly bounded in every compact subset of a region $ \Omega $, then it is a normal family.

The proof is based on Arzela-Ascoli Theorem.

If $ f $ is bounded, then by Cauchy-Integral, we get $ \mathcal{F} $ is equicontinuous on the subset. Then by AA Theorem, it's easy to show.

## Marty Theorem

A family of analytic or meromorphic functions f is normal in the classical sense if and only if the expressions

$$
\rho(f)=\frac{2|f^{'}(z)|}{1+|f(z)|^2}
$$

are locally bounded

### Some problems in Ahlfors

#### Problem P227 T1

Prove that in any region n the family of analytic functions with positive real part is normal. Under what added condition is it locally bounded ? Hint: Consider the functions $ e^{-f} $

##### Solution

Actually, we may use Marty Theorem by letting

$$
g(z)=\frac{f(z)-1}{f(z)+1}
$$

which is bounded. Then $ g^{'} $ is also locally bounded by using Cauchy Formula. Now you do the calculation.

#### Problem P227 T2

Show that the functions $ z^n $ , $ n $ a nonnegative integer, form a normal
family in $ |z| < 1 $ , also in $ |z| > 1 $ , but not in any region that contains a
point on the unit circle.

##### Solution

It's easy to show the first part. For the second, consider $ |a|=1 $. As soon as you show it's a normal family in region $ |z|<1 $ and $ |z|>1 $, then there exists a subsequence $ z^{n_k} $ which is convergent in the region contains a point on the unit circle. And this subsequence converges to $ \infty $ when $ |z|>1 $ and converges to $ 0 $ when $ |z|<1 $, which is contradict.

#### Problem P227 T3

If $ f(z) $ is analytic in the whole plane, show that the family formed
by all functions $f(kz) $ with constant $ k $ is normal in the annulus $ r_l < |z| < r_2 $
if and only if $ f(z) $ is a polynomial.

##### Solution

We can still use Marty Theorem. Since $ f(kz) $ is normal in the annulus. Then, by Marty Theorem, the expression

$$
\rho(f)=\frac{2k|f^{'}(z)|}{1+|f(z)|^{2}} < M\quad for \space some \space M
$$

It means $ |f^{'}| $ is bounded. Then it's trivial.

#### Problem P227 T4

If the family $ \mathcal{F} $ of analytic (or meromorphic) functions is not
normal in n, show that there exists a point $ Z_0 $ such that $ \mathcal{F} $ is not normal in
any neighborhood of $Z_0$ Hint: A compactness argument.

##### Solution

we prove by contradiction. That is near every point $ z $, $ \mathcal{F} $ is normal.
Use exhaustion: $ \Omega=\bigcup_{n=1}^{\infty}\Omega_n $, where $ \Omega_{n}\in \Omega_{n+1}$.We have a subsequence converging uniformly on $ \Omega_1 $ from it choose a subsequence converging uniformly on $ \Omega_2 $
, the process is infinite but the diagonal selection produces the desired subsequence.

### Singularity, Residue and some theorems

##### Riemann Theorem

If $f$ is a holomorphic function in an open set $\Omega$ except a point $z_0$. If f is bounded in $\Omega/\{z_0\}$ , then $z_0$ is the removable singularity of $f$

##### Corollory

Suppose $f$ has an isolated singularity $z_0$, and $|f|\to \infty$ . Then, $z_0$ is a pole of $f$

##### Casorati-Weierstrass

If $f$ is holomorphic in the punctured region $\Omega/ \{z_0\}$, where $z_0$ is a essential singularity. Then the image of $\Omega/ \{z_0\}$ under $f$ is dense.

##### The meromorphic functions in the extended complex planeare the rational functions

##### Argument Principle

$$
\frac{1}{2\pi i}\int_{\gamma}\frac{f(z)^{'}}{f(z)}dz=n(zeros)-n(poles)
$$

##### Rouche Theorem

if function $f$ is holomorphic in region $\Omega$ containing a circle $C$ and its interior. Then if

$$
|f|>|g|,\quad \forall z\in \partial C
$$

then $f$ and $f+g$ has the same number of zeros in $C$

##### Open mapping theorem

If $f$ is holomorphic and nonconstant in a region $\Omega$, then $f $ is open.

##### Maximum modulus principle

If $f $ is a non-constantholomorphic function in a region $\Omega$, then $f$ cannot attain a maximum in $\Omega$.
