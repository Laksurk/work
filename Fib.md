#### 斐波那契数列的几个性质

##### 记号与约定

对于数列 $\{a_n\}$，将其下标范围扩充到 $\Z$，规定当 $n<0$ 时 $a_n=0$. 

定义**斐波那契数列**（下简称 Fib）$\{f_n\}$ 为满足递推式 $f_n=f_{n-1}+f_{n-2}+[n=1]$ 的数列. 该数列的前几项为 $0,1,1,2,3,5,8$. 

规定数列 $\{g_n\}$ 的**生成函数**为多项式 $G(z)=\displaystyle\sum_ng_nz^n$. 

记 $[z^n]G(z)$ 表示生成函数 $G(z)$ 中 $z^n$ 项的系数. 则以下性质成立：

- $[z^n](F(z)\pm G(z))=[z^n]F(z)\pm[z^n]G(z)$.（可加性.）
- $[z^n](cG(z))=c[z^n]G(z)$.（齐次性，与上一条合称线性.）
- $[z^n](z^kG(z))=[z^{n-k}]G(z)$. 
- $[z^n]G'(z)=(n+1)[z^{n+1}]G(z)$. 

##### 等比数列的生成函数

考虑**等比数列** $\{g_n\}$ 由 $g_n=aq^n\ (n\in\N,\ a,q\in\R^*)$ 定义. 设 $\{g_n\}$ 的生成函数为 $G(z)$. 

写出 $\{g_n\}$ 的递推式 $g_n=qg_{n-1}+a[n=0]$，两边求和得
$$
\sum_n g_nz^n=q\sum_n g_{n-1}z^n+a\sum_n[n=0]z^n,
$$
化简得
$$
G(z)=qzG(z)+a,
$$
解得
$$
G(z)=\dfrac a{1-qz}.
$$

> 也可以倒推，直接对 $G(z)=\dfrac a{1-qz}$ 麦克劳林展开，即得到 $g_n=aq^n$. 

##### Fib 的生成函数

我们来求解 $F(z)=\displaystyle\sum_nf_nz^n=z+z^2+2z^3+3z^4+5z^5+\cdots$ 的封闭形式. 

由 $f_n=f_{n-1}+f_{n-2}+[n=1]$，两边求和得
$$
\sum_n f_nz^n=\sum_nf_{n-1}z^n+\sum_nf_{n-2}z^n+\sum_n[n=1]z^n,
$$
化简得
$$
F(z)=zF(z)+z^2F(z)+z,
$$
解得
$$
F(z)=\dfrac z{1-z-z^2}.
$$

##### Fib 的前缀和

设数列 $\{g_n\}$ 满足 $g_n=\displaystyle\sum_{i=0}^nf_i$，我们来求 $g_n$ 的通项. 

设 $\{g_n\}$ 的生成函数为 $G(z)$，有
$$
\begin{align}
G(z)=&\sum_n\sum_{i\le n}f_iz^n
\\=&\sum_if_i\sum_{n\ge i}z^n
\\=&\sum_if_iz^i\sum_{n\ge0}z^n
\\=&\dfrac1{1-z}F(z).
\end{align}
$$
于是 $G(z)$ 的封闭形式为 $G(z)=\dfrac z{(1-z)(1-z-z^2)}$. 用基本的裂项方法展开 $G(z)$：
$$
\begin{align}
G(z)=&\dfrac z{(1-z)(1-z-z^2)}
\\=&\dfrac1z(\dfrac{1}{1-z-z^2}-\dfrac{1}{1-z})
\\=&\dfrac1z(\dfrac{1}{1-z-z^2}-\dfrac{1}{1-z})
\\=&\dfrac1{z^2}F(z)-\dfrac1z\dfrac{1}{1-z}.
\end{align}
$$
于是
$$
\begin{align}
g_n=[z^n]G(z)=&f_{n+2}-1.
\end{align}
$$

##### Fib 的卷积

设数列 $\{g_n\}$ 满足 $g_n=\displaystyle\sum_if_if_{n-i}$，我们来求 $g_n$ 的通项. 

设 $\{g_n\}$ 的生成函数为 $G(z)$，有
$$
\begin{align}
G(z)=&\sum_n\sum_if_if_{n-i}z^n
\\=&\sum_n\sum_i(f_iz^i)(f_{n-i}z^{n-i})
\\=&(\sum_if_iz^i)(\sum_jf_{j}z^{j})
\\=&F^2(z).
\end{align}
$$
于是 $G(z)$ 的封闭形式为 $G(z)=\dfrac{z^2}{(1-z-z^2)^2}$. 为了求 $g_n$，可暴力展开 $G(z)$，但考虑到分母是一个四次式，这样做的计算量过大. 所以我们考虑用 $F(z)$ 凑出 $G(z)$ 来. 

注意到 $F'(z)=\dfrac{1+z^2}{(1-z-z^2)^2}$，这就得到了 $G(z)$ 的分母，但分子差一点. 配合 $\dfrac{F(z)}z=\dfrac{1-z-z^2}{(1-z-z^2)^2}$，$\left(\dfrac{F(z)}z\right)'=\dfrac{1+2z}{(1-z-z^2)^2}$，因为 $5z^2=3(1+z^2)-2(1-z-z^2)-(1+2z)$，就得到
$$
G(z)=\dfrac15(3F'(z)-2\dfrac{F(z)}z-\left(\dfrac{F(z)}z\right)').
$$
于是
$$
\begin{align}
g_n=[z^n]G(z)=&\dfrac15(3(n+1)f_{n+1}-2f_{n+1}-(n+1)f_{n+2})
\\=&\dfrac15(2nf_{n+1}-(n+1)f_n)
\\=&\dfrac15((n-1)f_{n+1}+(n+1)f_{n-1}).
\end{align}
$$

##### Fib 的封闭形式

> 记方程 $x^2-x-1=0$ 的两根为 $\phi=\dfrac{1+\sqrt5}2,\ \hat\phi=\dfrac{1-\sqrt5}2$. 有 $\phi\hat\phi=-1$、$\phi+\hat\phi=1$、$\phi-\hat\phi=\sqrt5$. $\phi\approx1.618$ 称作**黄金分割数**. 

我们已经知道 $\{f_n\}$ 的生成函数为 $F(z)=\dfrac{z}{1-z-z^2}$. 通过裂项，可以求得 $f_n$ 的封闭形式：
$$
\begin{align}
F(z)=&\dfrac z{1-z-z^2}
\\=&\dfrac{z}{(1-\phi z)(1-\hat\phi z)}
\\=&\dfrac1{\sqrt5}(\dfrac1{1-\phi z}-\dfrac1{1-\hat\phi z}),
\end{align}
$$
于是
$$
f_n=[z^n]F(z)=\dfrac1{\sqrt5}(\phi^n-\hat\phi^n).
$$

- 注意到 $\abs{\dfrac{\hat\phi^n}{\sqrt5}}<\dfrac12$，因此 $f_n=\lfloor\dfrac{\phi^n}{\sqrt5}\rceil$. 

- 不难证明，有递推式 $f_n=\phi f_{n-1}+\hat\phi^n$. 
