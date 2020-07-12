#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000 + 10;
const int MOD = 1000000007;

int T, n, k;
int a[MAXN];

int pow(int a, int b) { // a^b
    int ret = 1;
    while (b) {
        if (b & 1)
            ret = (long long) ret * a % MOD;
        a = (long long) a * a % MOD;
        b >>= 1;
    }
    return ret;
}

int sum(int a, int b) { // a^1+a^2+...+a^b
    if (b == 1) return a;
    int ret = (long long) sum(a, b >> 1) * (1 + pow(a, b >> 1)) % MOD;
    if (b & 1) {
        ret += pow(a, b);
        if (ret >= MOD) ret -= MOD;
    }
    return ret;
}

int main() {
    cin >> T;
    for (int cs = 1; cs <= T; ++cs) {
        long long x, y, c, d, e1, e2;
        int f;
        cin >> n >> k >> x >> y >> c >> d >> e1 >> e2 >> f;
        a[1] = (x + y) % f;
        for (int i = 2; i <= n; ++i) {
            int _x = (c * x + d * y + e1) % f;
            int _y = (d * x + c * y + e2) % f;
            x = _x;
            y = _y;
            a[i] = (x + y) % f;
        }

        int ans = 0;
        int s = 0; // (1^1+1^2+...+1^k)+(2^1+2^2+...+2^k)+...+(i^1+i^2+...+i^k)
        for (int i = 1; i <= n; ++i) {
            s += sum(i, k);
            if (s >= MOD) s -= MOD;
            ans += ((long long) a[i] * (n - i + 1) % MOD * s) % MOD;
            if (ans >= MOD) ans -= MOD;
        }
        cout << "Case #" << cs << ": " << ans << endl;
    }

    return 0;
}