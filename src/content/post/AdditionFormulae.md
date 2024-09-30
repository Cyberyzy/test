---
title: Addition Formular
publishDate: 2024-07-27 08:00:00
description: 'Introduction to addition formularrr~💩'
tags:
  - Complex Analysis
language: 'English'
---

<!--more-->

## The addition formular

Consider the map

$$
    z\to (1,\wp(z),\wp(z)^\prime)
$$

It parametrizes points on the cubic curve A defined by the equation

$$
    y^2=4x^3-g_2x-g_3
$$

The map is actually defined on the torus $\mathbb{C}/\Lambda$

Now for any complex number $\alpha$, $\wp(z)-\alpha$ has at most two zeros and at least one zero, so that already under $\wp$ we cover each complex number $\alpha$

Furthermore, $\mathbb{C}/\Lambda$ has a natural group structure, and we now want to see what it looks like when transported to A. We shall see that it's algebraic. In other words, if

$$
P_1=(x_1,y_1), \quad P_2=(x_2,y_2), \quad P_3=(x_3,y_3)
$$

and

$$
P_{3}=P_{1}+P_{2}
$$

then we shall express $x_3 , y_3$ as rational functions of $x_1 , y_1$ and $x_2 , y_2$. We shall see that $P_3$ is obtained by taking the line through $P_1,P_2$, intersecting it with the curve, and reflecting the point of intersection through the x-axis.
Select $u_1,u_2\in C$ and $\notin L$, and assume $u_1= u_2 (mod \lambda)$. Let a, b be complex numbers such that

$$
\begin{gathered}
\wp^{\prime}(u_{1}) =a\wp(u_1)+b \\
\wp^{\prime}(u_{2}) =a\wp(u_2)+b
\end{gathered}
$$

in other words $ y = ax + b $ is the line through $\wp^{\prime}(u_{1}) =a\wp(u_1)+b$,and $\wp^{\prime}(u_{2}) =a\wp(u_2)+b$.
Then

$$
\wp^{\prime}(z)-a\wp(z)-b
$$

has a pole of order 3 at 0, whence it has 3 zeros, counting multiplicities, and tow of these at $u_1,u_2$. If say $u_1$ had multiplicity 2, then

$$
    2u_1+u_2=0 (mod\space \lambda)
$$

and

$$
    u_3=-(u_1+u_2)(mod \space\lambda)
$$

the equation

$$
    4x^{3}-g_{2}x-g_{3}-(a x+b)^{2}=0
$$

has 3 roots. and

$$
    LHS=4(x-\wp(u_{1}))(x-\wp(u_{2}))(x-\wp(u_{3})).
$$

and you can get

$$
    \wp(u_1)+\wp(u_2)+\wp(u_3)=\frac{a^2}{4}
$$

we also have

$$
a(\wp(u*{1})-\wp(u_{2}))=\wp^{\prime}(u_{1})-\wp^{\prime}(u_{2})
$$

So

$$
    \wp(u_{3})=\wp(-(u_{1}+u_{2}))=\wp(u_{1}+u_{2})
$$

and we get

$$
    \wp(u_1+u_2)=-\wp(u_1)-\wp(u_2)+\frac{1}{4}\bigg(\frac{\wp'(u_1)-\wp'(u_2)}{\wp(u_1)-\wp(u_2)}\bigg)^2
$$

if we take limit as $u_1\to u_2$ and get

$$
 \wp(2u)=-2\wp(u)+\frac{1}{4}\bigg(\frac{\wp^{\prime\prime}(u)}{\wp^{\prime}(u)}
    \bigg)^2
$$

## geometric meaning of additional formulae

> Theorem
> The sum of 3 distinct points $ a, b, c $ on the elliptic curve is zero.

$$
a+b+c=0
$$

iff $ a, b, c $ lie on the projective line.

Proposition:
The following formular holds:

$$
\begin{vmatrix}
1 &\wp(u+v) & \wp^{\prime }(u+v)\\
1 &\wp(u) & \wp^{\prime }(u)\\
1 &\wp(v) &\wp^{\prime }(v)
\end{vmatrix}=0
$$

and

$$
\begin{array}{l}(x_1,y_1)=(\wp(u),\wp'(u)),\\ (x_2,y_2)=(\wp(v),\wp'(v)),\\ (x_3,y_3)=(\wp(u+v),-\wp'(u+v)).\end{array}
$$
