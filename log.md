### LOG

---

$$
{n\brace k}={n-1\brace k-1}+k{n-1\brace k}\\
\Delta_n\left(\dfrac1{k^{n}}{n\brace k}\right)=\dfrac1{k^{n+1}}{n\brace k-1}\\
\sum\dfrac1{k^{n+1}}{n\brace k-1}\delta n=\dfrac1{k^{n}}{n\brace k}+C\\
\sum\nolimits_0^n k^{n-x-1}{x\brace k-1}\delta x={n\brace k}-[k=0]\\
\sum_{i=0}^{n-1} k^{n-i-1}{i\brace k-1}={n\brace k}-[k=0]\\
\sum_{i=0}^{n-1} k^{n-i-1}{i\brace k-1}={n\brace k}-[k=0]\\
$$

上面那一堆没用，推着玩. 

---

$$
\mu(n)^2=\sum_{d^2\mid n}\mu(d)
$$
这个有用，就是把 $n$ 的质因数分解中指数为1的去掉（不贡献 $d$），指数大于2的变成2（不贡献 $\mu$），然后考虑 $d$ 取出 $k$ 个质数的情况数为 $\displaystyle\binom{m}{k}$ （$m$ 为质数个数），上述和就是 $\displaystyle \sum_{i=0}^m(-1)^{i}\binom mi=(1-1)^m=[m=0]$，当 $m=0$ 即无平方因子时为 $1$，否则为 $0$，恰好等于左边. 

这玩意可以求前缀和（SFN 计数）
$$
\begin{align}
\sum_{n=1}^N\mu(n)^2&=\sum_{n=1}^N\sum_{d^2\mid n}\mu(d)\\
&=\sum_d\mu(d)\sum_{n=1}^N[d^2\mid n]\\
&=\sum_d\mu(d)\lfloor\dfrac N{d^2}\rfloor\\
\end{align}
$$
正常求是根号，预处理 $S_\mu$ 整除分块是 $\Theta(n^{1/3})$. （题解说四次根号是不对的，不能简单认为整除分块就是开根号，要去类似根号分治地均值一下证不同数的个数的上界. 一般地，分母是求和变量的 $k$ 次方时复杂度是 $k+1$ 此根号，应该是这个结论吧我忘了. ）

次日补充：上面那一堆是啥玩意啊，我怎么用 $\mu$ 的通项把 $\mu*\mathrm{I}=\delta$ 证了一遍，我昨晚在想啥？？话说某些劣质博客里面出现过类似证明，是因为他们直接用通项定义 $\mu$，然后反过来用二项式定理证卷积式子. 真够反人类的. 

实际上就是反演嘛，哪有那么复杂，直接正常搞就完事了（写算法篇习题解答里了. ）

好数什么的也一样的. 所谓的枚举指数用 $\mu$ 当系数容斥不就是枚举最大指数的约数. 

又补充：最前面那个 $\mu$ 平方公式根本不用记，记了也没用，遇到一个记一个怎么可能记得完. 而且那个求和变量写得有迷惑性，应该写成 $d\mid \max\{d:d^2\mid n\}$，明白我的意思吧. 

补充上条：max里面的d和外面的d无甚关系，字母不够了. 

再次日补充：想出题. 

---

$$
\begin{align}
&\ \ \ \ \sum_{p\le\sqrt N}\log_pN\\
&=\sum_{p\le\sqrt N}\dfrac{\ln N}{\ln P}\\
&=\sum_{k}[k\ln k\le\sqrt N]\dfrac{\ln N}{\ln(k\ln k)}\\
\end{align}
$$

干啥呢. 不是瓶颈. 不要浪费时间. 

>QF P139 幸运数字 $\sigma$ 计数. 

尝试搞一下 DFS 的复杂度. 
$$
T(n,i)=
$$
搞不出来……这怎么能搞出来啊. 

能否放宽了毛估估，比如 $n$ 的 $\log n$ 个素因子随便组合，总共的组合数是贝尔数. OEIS A000110，貌似是指数级别的？……这不又回去了. 

是否n=奇素数的大于1次幂时都无解？

貌似没道理无解……懒得打表找规律了. 

---
