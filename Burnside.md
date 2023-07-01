### 从入门到 Burnside 引理

#### 〇、群

设集合 $G$ 上有二元运算 $*:G\times G\mapsto G$，若以下三个性质成立，则称 $(G,*)$ 构成**群**：

- **结合律**：$\forall a,b,c\in G$，$(ab)c=a(bc)$. 
- **幺元**：　$\exist e\in G$ 使得 $\forall a\in G$，$ea=ae=a$，称 $e$ 为幺元. 
- **逆元**：　$\forall a\in G$，$\exist a^{-1}\in G$ 使得 $a^{-1}a=aa^{-1}=e$，称 $a^{-1}$ 为 $a$ 的逆元. 

在无歧义时，通常简记 $(G,*)$ 为 $G$，$a*b$ 为 $ab$. 

若群 $G$ 有幺元 $e,e'$，必有 $e=ee'=e'$，因此幺元唯一. 类似地，容易证明任一元素 $a\in G$ 的逆元唯一，且左逆等于右逆. 

若 $H$ 是 $G$ 的子集，且 $(H,*)$ 也构成群，则称 $H$ 为 $G$ 的子群. 设 $H$ 有幺元 $e'$，则在 $G$ 中有 $e'=ee'=e$，故 $H$ 的幺元一定是 $G$ 的幺元. 因此，检验 $H$ 是子群，只需要检验以下性质：

- **封闭性**：$\forall a,b\in H$，$ab\in H$. 
- **幺元**：　$e\in H$. 
- **逆元**：　$\forall a\in H$，$a^{-1}\in H$. 

#### 一、同余

设群 $G$ 有子群 $H$，对 $a,b\in G$ 定义**同余**关系 $a\equiv b\Leftrightarrow a^{-1}b\in H$. 下验证 $\equiv$ 是 $G$ 上的一个**等价关系**：

- **自反性**：$a^{-1}a=e\in H$（子群包含幺元）. 
- **对称性**：$a^{-1}b\in H\Rightarrow b^{-1}a=(a^{-1}b)^{-1}\in H$（子群元素可逆）. 
- **传递性**：$a^{-1}b\in H\land b^{-1}c\in H \Rightarrow a^{-1}c=(a^{-1}b)(b^{-1}c)\in H$（子群封闭）. 

> 这里省略了 $(\mathrm{mod}\ H)$. 特别地，取 $G=\Z^+$，$H=m\Z$，此时 $\equiv(\mathrm{mod}\ m\Z)$ 即为数论中的 $\equiv (\mathrm{mod}\ m)$. 

若 $a\equiv b$，则称 $a$ 与 $b$ 属于同一个**等价类**. 由上述三个性质可知，所有等价类构成了 $G$ 的一个**划分**. 

> 集合上的一个等价关系确定一个划分，它是所有等价类的集合，集合的每个元素被恰好一个等价类包含. 

#### 二、陪集

首先引入群 $G$ 中元素与集合的乘法. 对 $a\in G$ 及 $K\sube G$ ，定义 $a$ 和 $K$ 的**（左）乘积**  $aK:=\{ak:k\in K\}$. 显然有 $eK=K$. 结合律 $a(bK)=(ab)K$ 成立，这是因为
$$
\begin{align}
a(bK)=a\{bk:k\in K\}=\{a(bk):k\in K\}=\{(ab)k:k\in K\}=(ab)K.
\end{align}
$$

由 $aK$ 的生成方式，$|aK|\le|K|$，但另一方面 $K=eK=(a^{-1}a)K=a^{-1}(aK)$，所以对称的结论 $|K|\le |aK|$ 也成立，因此 $|aK|=|K|$. 

> 形象地讲，由于群中元素均可逆，左乘 $a$ 并没有使 $K$ “丢失信息”. 

回到关于同余关系的讨论上来. 设群 $G$ 有子群 $H$，对 $a\in G$，考虑有哪些 $b$ 与 $a$ 同余：
$$
\begin{align}
a\equiv b&\Leftrightarrow a^{-1}b\in H
\\&\Leftrightarrow a^{-1}b=h,&\exist h\in H
\\&\Leftrightarrow b=ah,&\exist h\in H
\\&\Leftrightarrow b\in\{ah:h\in H\}
\\&\Leftrightarrow b\in aH.
\end{align}
$$

因此，$a$ 所在的等价类就是 $aH$. 我们称 $aH$ 为 $H$ 的一个**（左）陪集**. 陪集的集合 $G/H:=\{aH:a\in G\}$ 称作**商集**，它就是同余关系 $\equiv$ 所确定的 $G$ 的划分. 商集的大小 $|G/H|$ 也称**指数**，记作 $[G:H]$，它就是等价类（陪集）的个数. 

> 这里默认 $G$ 是有限群，下同. 

由之前我们证明的，$|aH|=|H|$，可知所有陪集都一样大. 而这些陪集构成对 $G$ 的划分（不重不漏地包含 $G$ 的每个元素），因此陪集数乘陪集大小就等于 $G$ 的大小，即
$$
|G|=|H|[G:H]. 
$$
这便是**拉格朗日定理**. 

#### 三、群作用

对非空集合 $S$，在 $S$ 上可定义**映射** $S\mapsto S$. 设群 $G$ 是由若干映射 $g:S\mapsto S$ 和映射的**复合**运算 $\circ$ 构成的群. 

- **结合律**：$h\circ (g\circ f)=(h\circ g)\circ f$ 总是成立，这是因为两边都把 $s\in S$ 映到 $h(g(f(s)))$. 
- **幺元**：　恒等映射 $\mathrm{id}_S\in G$ 把任何一个 $s\in S$ 映到自身，有 $f\circ\mathrm{id}_S=\mathrm{id}_S\circ f=f$. 
- **逆元**： 　$G$ 中元素可逆，因此这些映射都是**双射**，称作 $S$ 上的**变换**（因 $S$ 是有限集，也称**置换**）. 对 $f\in G$，$f$ 的逆元就是其逆映射 $f^{-1}$，有 $f\circ f^{-1}=f^{-1}\circ f=\mathrm{id}_S$. 

映射的复合是群 $G$ 元素的乘积，因此 $g\circ f$ 通常简写成 $gf$；恒等映射 $\mathrm{id}_S$ 是群 $G$ 的幺元，因此也记作 $e$. $f(s)$ 又称元素 $f$ 对 $s$ 的**作用**，省略括号记成 $fs$. 这样，群 $G$ 在 $S$ 上的**作用**满足两条性质：

- 幺元是恒等映射：$es=s$. 
- 结合律：$g(fs)=(gf)s$. 

对于**置换群** $G$，集合 $S$ 又称**指标**集合. 

#### 四、轨道

设群 $G$ 作用于集合 $S$. 现在固定某个 $s\in S$，我们来研究 $G$ 的元素对 $s$ 的作用. 

考虑 $G$ 中每个元素对 $s$ 的作用，它们构成的集合称为 $s$ 的**轨道**，记作 $O_s$，即 $O_s:=\{gs:g\in G\}$. $O_s$ 是 $S$ 的子集. 

> 模仿之前对元素和集合的乘法的记号，$s$ 的轨道理应记作 $Gs$，代表每个 $g\in G$ 与 $s$ 的乘积，然而这个符号跟稳定子 $G_s$ 过于相似，还是不要用为好. 

下面我们来说明，$S$ 的所有元素的轨道构成 $S$ 的划分. 

- **自反性**：$s=es\in O_s$. 
- **对称性**：$t\in O_s\Rightarrow t=gs,\ \exist g\in G\Rightarrow s=g^{-1}t,\ \exist g\in G\Rightarrow s\in O_t$. 
- **传递性**：$p\in O_t\land t\in O_s\Rightarrow p=gt\land t=fs,\ \exist g,f\in G\Rightarrow p=(gf)s,\ \exist g,f\in G\Rightarrow p\in O_s$. 

#### 五、稳定子

设群 $G$ 作用于集合 $S$，依然固定某个 $s\in S$，研究 $G$ 的元素对 $s$ 的作用. 

考虑所有使 $s$ 不变的映射 $g\in G$，它们构成的集合称为 $s$ 的**稳定子**，记作 $G_s$，即 $G_s:=\{g\in G:gs=s\}$. 下面我们来证明，$G_s$ 是 $G$ 的子群. 

- **封闭性**：$gs=s\land fs=s\Rightarrow (gf)s=s$. 
- **幺元**：　$es=s$. 
- **逆元**：　$gs=s\Rightarrow g^{-1}gs=g^{-1}s\Rightarrow s=g^{-1}s$. 

既然稳定子 $G_s$ 是一个子群，如前所述，它的所有陪集确定了 $G$ 的划分 $G/G_s$. 

依据对 $s$ 的作用是否相同（显然这是个等价关系），可以确定 $G$ 的一个划分. 对 $g,f\in G$，
$$
\begin{align}
gs=fs&\Leftrightarrow f^{-1}gs=f^{-1}fs
\\&\Leftrightarrow (f^{-1}g)s=s
\\&\Leftrightarrow f^{-1}g\in G_s
\\&\Leftrightarrow g\equiv f\ (\mathrm{mod}\ G_s).
\end{align}
$$
因此，这个划分就是 $G/G_s$！换句话说，$G_s$ 的陪集内的映射将 $s$ 映到同一元素，陪集间的映射将 $s$ 映到不同元素.（此处应有一张图片.） $O_s$ 中的元素与 $G_s$ 的陪集一一对应，即
$$
|O_s|=[G:G_s].
$$
这就是**轨道稳定子定理**. 

代入拉格朗日定理 $|G|=|G_s|[G:G_s]$，我们有
$$
|G|=|G_s||O_s|.
$$
轨道大小乘稳定子大小等于 $G$ 的大小. 

#### 六、Burnside 引理

设群 $G$ 作用于集合 $S$. 现在希望对 $S$ 的等价类计数，即求轨道数. 通常对等价类计数的方式是计算代表元的数量，即让代表元贡献 $1$，其他元素贡献 $0$，但此时这种方法难以起效. 好在，轨道大小是容易求得的，因此我们让每个元素 $s$ 贡献恰好 $\dfrac1{|O_s|}$ 即可. 则轨道数为
$$
\begin{align}
&\sum_{s\in S}\dfrac1{|O_s|}
\\=&\sum_{s\in S}\dfrac{|G_s|}{|G|}
\\=&\dfrac1{|G|}\sum_{s\in S}|G_s|
\\=&\dfrac1{|G|}\sum_{\substack{s\in S\\g\in G}}[gs=s]
\\=&\dfrac1{|G|}\sum_{g\in G}|S_g|.
\end{align}
$$
其中 $S_g:=\{s\in S:gs=s\}$，$|S_g|$ 为映射 $g$ 的**不动点**数量.  这样计数尤其适合 $S$ 非常大而 $G$ 比较小的情境，此时虽然轨道数非常多，但是只需要枚举 $g\in G$ 就能计算轨道数. 这就是 **Burnside 引理**. 

#### 小结

- 由子群 $H$ 定义的同余 $\equiv$ 是群 $G$ 上的等价关系，其确定的划分是商集（陪集的集合）$G/H$. 
- $H$ 的所有陪集都等势，这给出拉格朗日定理 $|G|=|H|[G:H]$. 
- 一个置换群 $G$ 作用于指标集 $S$ 上，$s$ 的所有像构成轨道 $O_s$，稳定 $s$（使 $s$ 不动）的所有 $g$ 构成稳定子 $G_s$. 
- 稳定子 $G_s$ 是 $G$ 的子群，它的每个陪集对应 $s$ 的一个像，这给出轨道稳定子定理 $[G:G_s]=|O_s|$. 
- $S$ 中的所有轨道是 $S$ 的划分，轨道 $O_s$ 是 $s$ 所在的等价类，由此对轨道计数得到 Burnside 引理. 

Burnside 引理：群 $G$ 作用于集合 $S$，将 $S$ 划分成若干个轨道，则轨道数是群 $G$ 所有元素不动点数目的平均值. 

适用于等价关系定义简单的等价类计数问题. 

#### 习题

##### 【洛谷 P4980】

设全体染色方案组成状态空间 $S$，$n$ 种染色方案上的旋转组成群 $G$，则所求本质不同方案数即为 $G$ 作用于 $S$ 的轨道数. 

设 $g_i\in G$ 表示旋转 $i$ 格的变换. 由初等数论常识，将 $n$ 元环转过 $i$ 格，构成了 $n$ 个格上的 $\mathrm{gcd}(n,i)$ 个循环. 若某状态是 $g_i$ 的不动点，则其每个循环必须填同一种颜色. 于是 $g_i$ 的不动点数为 $n^{\mathrm{gcd}(n,i)}$. 

由 Burnside 引理，轨道数为
$$
\begin{align}
&\dfrac1n\sum\limits_{i=1}^nn^{\gcd(n,i)}
\\=&\dfrac1n\sum_g\sum\limits_{i=1}^nn^g[g\mid n][g\mid i][\dfrac ng\perp\dfrac ig]
\\=&\dfrac1n\sum_{g\mid n} n^g\sum\limits_{i=1}^{n/g}[\dfrac ng\perp i]&(gi\leftarrow i)
\\=&\dfrac1n\sum_{g\mid n} n^g\phi(\dfrac ng)
\end{align}
$$
通过对 $n$ 分解质因数求解上式，复杂度 $O(\sqrt n)$. 

> 这题也可以用 $\mu$ 容斥解决，留做习题. 

##### 【洛谷 P1446】

设全体染色方案组成状态空间 $S$，由题意，添加恒等置换后，$m+1$ 种洗牌方案构成群 $G$，则所求即为 $G$ 作用于 $S$ 的轨道数. 

洗牌方案 $g\in G$ 是在 $n$ 张牌上的置换，设其有 $i$ 个循环. 若某状态是 $g$ 的不动点，则每个循环必须染成相同颜色. 考虑每种颜色出现的次数是给定的，需要用 dp 求出 $g$ 的不动点数. 

具体 dp 过程略. 

##### 【洛谷 P4727】

设全体 $n$ 个点的有标号无向图（看成一个对角线全为 $0$ 的对称0/1矩阵）组成状态空间 $S$，点标号上的全体置换构成群 $G$，则所求即为 $G$ 作用于 $S$ 的轨道数. 

