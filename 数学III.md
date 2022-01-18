### 数学 III

#### （一）偏序

**【定义 1】**对于集合 $X$ 与 $Y$，称 $X\times Y = \left\{(x,y):x\in X, y\in Y\right\}$ 为集合 $X$ 与 $Y$ 的**直积**，又称**笛卡尔积**。

> 例如 $\{1,2\}\times\{a,b,c\}=\{(1,a),(1,b),(1,c),(2,a),(2,b),(2,c)\}$。

**【定义 2】**对于集合 $X$，若 $R$ 为 $X\times X$ 的一个子集，则称 $R$ 为 $X$ 上的一个**二元关系**。对于 $x,y\in X$，若 $(x,y)\in R$，则称 $x$ 与 $y$ **满足关系** $R$，记作 $xRy$；反之则称 $x$ 与 $y$ **不满足关系** $R$，记作 $x\not Ry$。

**【定义 3】** 对于集合 $X$ 和其上的二元关系 $R$，$R$ 可能具有以下性质：

1. **自反性**： &emsp;$\forall x\in X$，$xRx$；
2. **反自反性**： $\forall x\in X$，$x\not Rx$；
3. **对称性**： &emsp;$\forall x,y\in X$，$xRy \Rightarrow yRx$；
4. **反对称性**： $\forall x,y\in X$，$x\ne y \land xRy \Rightarrow y\not Rx$；
5. **传递性**： &emsp;$\forall x,y,z\in X$，$xRy \land yRz \Rightarrow xRz$。

**【定义 4】**对于集合 $X$ 和其上的二元关系 $R$，若 $R$ 满足自反性、反对称性和传递性，则称 $R$ 是集合 $X$ 的**偏序关系**，简称**偏序**，记为 $\preccurlyeq$；称 $(X,\preccurlyeq)$ 为**偏序集**。

> 此时 $\preccurlyeq$ 即为 $R$，二者是相同的：$xRy$ 也即 $x\preccurlyeq y$。

**【定义 5】**对于偏序集 $(X,\preccurlyeq)$，对于 $x,y\in X$，若 $x\preccurlyeq y\land x\neq y$，则称 $x$ 与 $y$ 满足**严格偏序关系**，记为 $x\prec y$。

> 易证，$\prec$ 为 $X$ 上的一个满足反自反性、反对称性和传递性的二元关系。

**【定义 6】**对于偏序集 $(X,\preccurlyeq)$，对于 $x,y\in X$，若 $x\preccurlyeq y \lor y\preccurlyeq x$，则称 $x$ 与 $y$ **可比**；反之则称 $x$ 与 $y$ **不可比**。若 $\forall x,y\in X$，$x$ 与 $y$ 均可比，则称 $\preccurlyeq$ 为一个**全序关系**。

> 如 $X=\left\{1,2,3\right\}$ 时，$\leqslant$ 是全序关系，但 $<$ 不是。

#### （二）卷积与逆函数

**【定义 1】**对于偏序集  $(X,\preccurlyeq)$，对于二元函数 $f:X\times X\rightarrow \R$，若 $\forall x\npreceq y$ 都有  $f(x,y)=0$，则称 $f$ 为一个**“好函数”**；记所有 $X$ 上的“好函数”的集合为 $\cal F$$(X)$。

**【定义 2】**对于 $f,g\in \cal F$$(X)$，定义 $f,g$ 的**卷积** $h=f*g$ $(h\in \cal F$$(X))$ 为
$$
h(x,y)=\left\{\begin{array}{l}
\sum\limits_{z:x\preccurlyeq z\preccurlyeq y}f(x,z)g(z,y) & x\preccurlyeq y\\
0 & \mathrm{otherwise}
\end{array}\right.
$$

**【定理 1】**$(f*g)*h=f*(g*h)$，即**卷积满足结合律**。

> **证明&emsp;**利用卷积定义展开式子，交换求和顺序即可。
> $$
> \begin{align}&((f*g)*h)(x,y)\\
> =&\sum\limits_{z:x\preccurlyeq z\preccurlyeq y}(\sum\limits_{u:x\preccurlyeq u\preccurlyeq z}f(x,u)g(u,z))h(z,y)\\
> =&\sum\limits_{z:x\preccurlyeq z\preccurlyeq y}\sum\limits_{u:x\preccurlyeq u\preccurlyeq z}f(x,u)g(u,z)h(z,y)\\
> =&\sum\limits_{z:x\preccurlyeq z\preccurlyeq y}\sum\limits_{u}[x\preccurlyeq u\preccurlyeq z]f(x,u)g(u,z)h(z,y)\\
> =&\sum\limits_{u}\sum\limits_{z:x\preccurlyeq z\preccurlyeq y}[x\preccurlyeq u\preccurlyeq z]f(x,u)g(u,z)h(z,y)\\
> =&\sum\limits_{u:x\preccurlyeq u\preccurlyeq y}\sum\limits_{z:u\preccurlyeq z\preccurlyeq y}f(x,u)g(u,z)h(z,y)\\
> =&\sum\limits_{u:x\preccurlyeq u\preccurlyeq y}f(x,u)\sum\limits_{z:u\preccurlyeq z\preccurlyeq y}g(u,z)h(z,y)\\
> =&\sum\limits_{u:x\preccurlyeq u\preccurlyeq y}f(x,u)(g*h)(u,z)\\
> =&(f*(g*h))(x,y)
> \end{align}
> $$

**【定义 3】**对于偏序集 $(X,\preccurlyeq)$，定义 $\delta(x,y)=[x=y]$ $(\delta\in\cal F$$(X))$。

> 若命题 $P$ 成立，则 $[P]=1$；否则 $[P]=0$。

**【定理 2】**$\forall f\in \cal F$$(X)$，$\delta*f=f*\delta=f$。

> **证明&emsp;**由卷积的定义，这是显然的。

**【定义 4】**对于 $f\in \cal F$$(X)$ 且满足 $\forall x\in X$，$f(x,x)\ne0$。若 $g*f=\delta$ $(g\in \cal F$$(X))$，则称 $g$ 为 $f$ 的**左逆函数**；若 $f*g=\delta$，则称 $g$ 为 $f$ 的**右逆函数**。

**【定理 3】**$\forall f\in\cal F$$(X)$，$f$  的左逆函数 $g$ 的递推式为
$$
g(x,y)=\left\{\begin{array}{l}
\dfrac1{f(y,y)} & x=y\\
-\dfrac1{f(y,y)}\sum\limits_{z:x\preccurlyeq z\prec y}g(x,z)f(z,y) & x\prec y\\
0 & \mathrm{otherwise}
\end{array}\right.
$$

$f$  的右逆函数 $h$ 的递推式为
$$
h(x,y)=\left\{\begin{array}{l}
\dfrac1{f(y,y)} & x=y\\
-\dfrac1{f(y,y)}\sum\limits_{z:x\preccurlyeq z\prec y}f(x,z)h(z,y) & x\prec y\\
0 & \mathrm{otherwise}
\end{array}\right.
$$

> **证明&emsp;**直接根据逆函数的定义展开卷积后解得。

因此，**左、右逆函数存在且唯一**。

**【定理 4】** $\forall f\in\cal F$$(X)$，$f$  的**左、右逆函数相同**。

> **证明&emsp;**设 $f$ 的左、右逆函数分别为 $g$、$h$，即 $g*f=f*h=\delta$
>
> 则 $(g*f)*h=\delta*h$
>
>$\therefore g*(f*h)=h$
>
>$\therefore g*\delta=h$
>
>$\therefore g=h$

因此将左右逆函数统称为**逆函数**。即：**任意一个 $f\in\cal F$$(X)$ 必有唯一的逆函数 $g$，使得 $f*g=g*f=\delta$。**

#### （三）广义莫比乌斯反演

**【定义 1】**对于偏序集 $(X,\preccurlyeq)$，定义 $\zeta(x,y)=[x\preccurlyeq y]$ $(\zeta\in\cal F$$(X))$；定义 $\mu$ 为 $\zeta$ 的反函数，即 $\mu*\zeta=\zeta*\mu=\delta$。称 $\mu$ 为 $(X,\preccurlyeq)$ 上的**莫比乌斯函数**。

> 显然，$\mu(x,x)=1$；且对于 $x\npreceq y$，$\mu(x,y)=0$。

**【定理 1】**对于偏序集  $(X,\preccurlyeq)$，若 $x\prec y$，则有
$$
\sum\limits_{z:x\preccurlyeq z\preccurlyeq y}\mu(x,z)=\sum\limits_{z:x\preccurlyeq z\preccurlyeq y}\mu(z,y)=0
$$

> **证明&emsp;**分别将 $\mu*\zeta$ 和 $\zeta*\mu$ 展开，化简式子易得。

**【定理 2】莫比乌斯反演公式**：对于有限偏序集 $(X,\preccurlyeq)$，若函数 $F$、$G:X\rightarrow\R$ 满足
$$
G(x)=\sum\limits_{z:z\preccurlyeq x}F(z)
$$
则有：
$$
F(x)=\sum\limits_{y:y\preccurlyeq x}G(y)\mu(y,x)
$$
> **证明&emsp;**将 $G(y)$ 代入，交换求和顺序，然后根据 $\mu$ 函数的定义简化式子即可。
> $$
> \begin{align}&\sum\limits_{y:y\preccurlyeq x}G(y)\mu(y,x)\\
> =& \sum\limits_{y:y\preccurlyeq x}\sum\limits_{z:z\preccurlyeq y}F(z)\mu(y,x)\\
> =& \sum\limits_{y:y\preccurlyeq x}\sum\limits_{z}[z\preccurlyeq y]F(z)\mu(y,x)\\
> =& \sum\limits_{z}F(z)\sum\limits_{y:y\preccurlyeq x}[z\preccurlyeq y]\mu(y,x)\\
> =& \sum\limits_{z}F(z)\sum\limits_{y:z\preccurlyeq y\preccurlyeq x}\zeta(z,y)\mu(y,x)\\
> =& \sum\limits_{z}F(z)\delta(z,x)\\
> =& F(x)
> \end{align}\\
> $$

#### （四）狭义莫比乌斯反演

**【定义 1】**对于偏序集 $(X,\preccurlyeq_1)$、$(Y,\preccurlyeq_2)$，设集合 $X\times Y$ 上有二元关系 $R=\{((x,y),(x',y')):x\preccurlyeq_1x', y\preccurlyeq_2y'\}$，称 $(X\times Y,R)$  为这两个**偏序集的直积**。

> 易证，$R$ 为偏序关系，即**偏序集的直积还是偏序集**。将 $R$ 写为 $\preccurlyeq$，则有
> $$
> (x,y)\preccurlyeq(x',y')\iff x\preccurlyeq_1x'\land y\preccurlyeq_2y'
> $$

**【定理 1】**对于偏序集 $(X,\preccurlyeq_1)$、$(Y,\preccurlyeq_2)$，设其上的莫比乌斯函数分别为 $\mu_1$、$\mu_2$，设这两个偏序集的直积 $(X\times Y,\preccurlyeq)$ 上的莫比乌斯函数为 $\mu$，则有
$$
\mu((x,y),(x',y'))=\mu_1(x,x')\mu_2(y,y')
$$
> **证明&emsp;**若 $x\prec x'\land y\prec y'$ 不成立，根据 $\mu$ 的定义很容易证明，故只需证其成立的情况。
> $$
> \begin{align} & \mu((x,y),(x',y'))\\
> =& -\sum\limits_{(u,v):(x,y)\preccurlyeq (u,v)\prec (x',y')}\mu((x,y),(u,v))\\
> =& -\sum\limits_{(u,v):(x,y)\preccurlyeq (u,v)\preccurlyeq (x',y')}\mu((x,y),(u,v)) + \mu((x,y),(x',y'))\\
> =& -\sum\limits_{u:x\preccurlyeq u\prec x'}\sum\limits_{v:y\preccurlyeq v\prec y'}\mu((x,y),(u,v))
> \end{align}
> $$

**【定义 2】**定义集合 $X_n = \{1,2,3,\cdots,n\}(n\in\Z^+)$，偏序集 $D_n=(X_n,|)$。

> $|$ 表示整除运算。易证，$|$ 是偏序关系。

**【定理 2】**对于偏序集 $D_n$，$\forall a,b\in X_n$，若 $a|b$，则 $\mu(a,b)=\mu(1,\dfrac ba)$。

> **证明&emsp;**我不会证，故略。

> 这启发我们，$D_n$ 上第一个参数为 $1$ 的 $\mu$ 函数有较大价值。

**【定理 3】**对于偏序集 $D_n$，有
$$
\mu(1,n)=\left\{\begin{array}{l}
1 & n=1\\
(-1)^k & n=p_1p_2\cdots p_k,\ \ p_i\ne p_j(i\ne j)\\
0 & \mathrm{otherwise}
\end{array}\right.
$$

> **证明&emsp;**将 $n$ 质因数分解为 $n=p_1^{a_1}p_2^{a_2}\cdots p_k^{n_k}$。

