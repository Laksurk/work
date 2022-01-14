### 数学 III

#### （一）偏序

**【定义 1】**对于集合 $X$、$Y$，称 $X\times Y = \left\{(x,y):x\in X,y\in Y\right\}$ 为 $X$ 与 $Y$ 的**笛卡尔积**。

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

> 如 $X=\left\{1,2,3\right\}$ 时，$\le$ 是全序关系，但 $<$ 不是。

#### （二）卷积与逆函数

**【定义 1】**对于偏序集  $(X,\preccurlyeq)$，对于二元函数 $f:X\times X\rightarrow \R$，若 $\forall x\npreceq y$ 都有  $f(x,y)=0$，则称 $f$ 为一个**“好函数”**；记所有 $X$ 上的“好函数”的集合为 $\cal F$$(X)$。

**【定义 2】**对于 $f,g\in \cal F$$(X)$，定义 $f,g$ 的**卷积** $h=f*g$ $(h\in \cal F$$(X))$ 为
$$
h(x,y)=\left\{\begin{array}{}
\sum\limits_{z:x\preccurlyeq z\preccurlyeq y}f(x,z)g(z,y) & x\preccurlyeq y\\
0 & \mathrm{otherwise}
\end{array}\right.
$$

**【定理 1】**$(f*g)*h=f*(g*h)$，即**卷积满足结合律**。

**证明&emsp;**略

**【定义 3】**定义 $\delta(x,y)=[x=y]$ $(\delta\in\cal F$$(X))$。

> 若命题 $P$ 成立，则 $[P]=1$；否则 $[P]=0$。

**【定理 2】**$\forall f\in \cal F$$(X)$，$\delta*f=f*\delta=f$。

**证明&emsp;**由卷积的定义，这是显然的。

**【定义 4】**对于 $f\in \cal F$$(X)$ 且满足 $\forall x\in X$，$f(x,x)\ne0$。若 $g*f=\delta$ $(g\in \cal F$$(X))$，则称 $g$ 为 $f$ 的**左逆函数**；若 $f*g=\delta$，则称 $g$ 为 $f$ 的**右逆函数**。

**【定理 3】左、右逆函数存在且唯一**。

**证明&emsp;**根据左逆函数的定义解得

$$
g(x,y)=\left\{\begin{array}{}
\dfrac1{f(y,y)} & x=y\\
-\dfrac1{f(y,y)}\sum\limits_{z:x\preccurlyeq z\prec y}g(x,z)f(z,y) & x\prec y\\
0 & \mathrm{otherwise}
\end{array}\right.
$$
右逆函数同理。

**【定理 4】左逆函数与右逆函数相同**。

**证明&emsp;**设 $f$ 的左、右逆函数分别为 $g$、$h$，即 $g*f=f*h=\delta$

则 $(g*f)*h=\delta*h$

$\therefore g*(f*h)=h$

$\therefore g*\delta=h$

$\therefore g=h$

因此，我们将左、右逆函数统称为**逆函数**。

> 小结：任意一个 $\cal F$$(X)$ 中的函数 $f$ 必有唯一的逆函数 $g$，使得 $f*g=g*f=\delta$。

#### （三）$\mu$ 函数与莫比乌斯反演

【定义 1】$\zeta$ 函数和 $\mu$ 函数

【定理 1】莫比乌斯反演公式

#### （四）

