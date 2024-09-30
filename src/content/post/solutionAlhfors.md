---
title: Solution to Alhfors
publishDate: 2023-05-11 22:51:21
tags:
  - Complex Analysis
description: 'Solution to Alhfors Complex Analysis'
language: 'English'
---

Alhfors Complex Analysis 的习题答案，主要是椭圆函数这一节。

## P274 Exercise 1

The Weierstrass functions satisfy numerous identities which are best dealt with in an exercise section. They can be proved either by comparing two elliptic functions with the same zeros and poles (when $ \sigma $ -functions are involved), or by comparing elliptic functions with the same singular parts (when only $ \wp $ and $ \zeta $ -functions are involved). The following sequence of formulas is so arranged that we need to resort to this method only once.

## Solution 1

$$
    \wp(z)-\wp(u)=-\frac{\sigma(z-u)\sigma(z+u)}{\sigma(z)^2\sigma(u)^2}
$$

依据提示，我们考虑利用3.2节的(14)式，即

$$
    \begin{gathered}
\sigma(z+\omega_1) =-\sigma(z)e^{\eta_1(z+\omega_1/2)} \\\\
\sigma(z+\omega_2) =-\sigma(z)e^{\eta_2(z+\omega_2/2)}.
\end{gathered}
$$

证明右侧式的周期为$ \omega_1,\omega_2 $
事实上

$$
\begin{align*}
\phi(z+\omega_1)&=-\frac{\sigma(z-u+\omega_1)\sigma(z+u+\omega_1)}{\sigma(z+\omega_1)^2\sigma(u)^2} \\\\
&=-\frac{\sigma(z-u)\sigma(z+u)e^{2\eta_1z+\eta_1\omega_1}}{\sigma(z)^2\sigma(u)^2e^{2\eta_1(z+\omega_1/2)}}\\\\
&=-\frac{\sigma(z-u)\sigma(z+u)}{\sigma(z)^2\sigma(u)^2}\\\\
&=\phi(z)
\end{align*}
$$

同理可证$ \omega_2 $ 也为$ \phi(z) $ 的周期。
我们再考虑$ \phi(z) $ 的零极点
显然左式的零点为$ \pm u $, 仅有的二阶极点为原点。
对于右式，有\

$$ \phi(u)=\phi(-u)=0 $$

且$ \phi(z) $的极点为 $ \sigma(z)$ 的零点。由定义可知为$ z=0 $,且是二阶极点。
综上可知
 $$
    \wp(z)-\wp(u)=-\frac{\sigma(z-u)\sigma(z+u)}{\sigma(z)^2\sigma(u)^2}
$$

## P274 Exercise 2

Prove
$$
    \frac{\wp'(z)}{\wp(z)-\wp(u)}=\zeta(z-u)+\zeta(z+u)-2\zeta(z)
$$

Follows from (16) by taking logarithmic derivatives.

## Solution 2

 依据提示，我们考虑利用上面的结论，对两边求对数导数，即
 $$
    \begin{align*}
    &\frac{\wp'(z)}{\wp(z)-\wp(u)}\\\\
    &=\frac{(\sigma(z-u)^{\prime}\sigma(z+u)+\sigma(z-u)\sigma(z+u)^{\prime})}{\sigma(z+u)\sigma(z-u)}\\\\
    &-2\frac{\sigma(z+u)\sigma(z-u)\sigma(z)^{\prime}}{\sigma(z)\sigma(z+u)\sigma(z-u)}\\\\
    &=\zeta(z-u)+\zeta(z+u)-2\zeta(z)
    \end{align*}
 $$
 证毕

## P274 Exercise 3

Prove
$$
    \zeta(z+u)=\zeta(z)+\zeta(u)+\frac{1}{2}\frac{\wp'(z)-\wp'(u)}{\wp(z)-\wp(u)}
$$

This is a symmetrized version of (17).

## Solution 3

事实上，对换 Exercise 2中$ z $ 和$ u $ 的位置可以得到
$$
      \frac{\wp'(u)}{\wp(u)-\wp(z)}=\zeta(u-z)+\zeta(u+z)-2\zeta(u)
$$
则有
$$
\begin{align*}
    \frac{1}{2}\frac{\wp'(z)-\wp'(u)}{\wp(z)-\wp(u)}&=\zeta(u+z)+\frac{1}{2}(\zeta(u-z)+\zeta(z-u))\\\\
    &-(\zeta(u)+\zeta(z))\\\\
    &=\zeta(u+z)-(\zeta(u)+\zeta(z))
\end{align*}
$$
移项即得。

## P277 Exercise 5

Prove $$
    \wp(2z)=\frac{1}{4}\left(\frac{\wp''(z)}{\wp'(z)}\right)^2-2\wp(z)
$$

## Solution 5

考虑使用加法公式
$$
    \wp(z+u)=-\wp(z)-\wp(u)+\frac{1}{4}\bigg(\frac{\wp'(z)-\wp'(u)}{\wp(z)-\wp(u)}\bigg)^2
$$

令$ u=z+\Delta z $,则
$$
\begin{align*}
    \wp(2z+\Delta z)&=-\wp(z)-\wp(z+\Delta z)\\\\
    &+\frac{1}{4}\bigg(\frac{\wp'(z)-\wp'(z+\Delta z)}{\wp(z)-\wp(z+\Delta z)}\bigg)^2\\\\
\end{align*}
$$

而
$$
    \lim_{\Delta z\to 0}-\wp(z)-\wp(z+\Delta z)=-2\wp(z)
$$

$$
\begin{align*}
    \frac{1}{4}\bigg(\frac{\wp'(z)-\wp'(z+\Delta z)}{\wp(z)-\wp(z+\Delta z)}\bigg)^2&=\frac{1}{4}\bigg(\frac{(\wp'(z)-\wp'(z+\Delta z))/\Delta z}{(\wp(z)-\wp(z+\Delta z))/\Delta z}\bigg)^2\\\\
&=\frac{1}{4}\left(\frac{\wp''(z)}{\wp'(z)}\right)^2\quad \Delta z\to 0
\end{align*}
$$

则$$
    \wp(2z)=\frac{1}{4}\left(\frac{\wp''(z)}{\wp'(z)}\right)^2-2\wp(z)
$$

## P277 Exercise 6

Prove
$$
    \wp'(z)=-\sigma(2z)/\sigma(z)^4
$$

## Solution 6

注意到右侧极点为$ z=0 $,且为3阶极点，而零点则为$$
    \frac{\omega_1}{2},\space\frac{\omega_2}{2},\space\frac{\omega_1+\omega_2}{2}
$$
事实上有$$
    -\sigma(\omega_1)/\sigma(\omega_1/2)^4=-\frac{\sigma(0)e^{\eta_1\omega_1/2}}{\sigma(\omega_1/2)^4}=0
$$

同理可证其余情况。
而周期性是显然的，由式(14)立得
$$
\begin{align*}
    -\sigma(2z+2\omega_1)/\sigma(z+\omega_1)^4&=-\frac{\sigma(2z)e^{4\eta_1z+2\eta_1\omega_1}}{\sigma(z)^4e^{4\eta_1(z+\omega_1/2)}}\\\\
    &=-\sigma(2z)/\sigma(z)^4
\end{align*}
$$

同理可证$ \omega_2 $也是周期， 由此可得
$$
    \wp'(z)=-\sigma(2z)/\sigma(z)^4
$$
