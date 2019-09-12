// Problem
// You have been hired recently as the Chief Decision Maker (CDM) at a famous parcel delivery company, congratulations! 
// Customers love speedy deliveries of their parcels and you have decided to decrease the time it takes to deliver parcels 
// around the world to win customers. 
// You have introduced this idea to the authorities and they have allocated you enough budget 
// to build at most one new delivery office.
// The world can be divided into an R × C grid of squares. 
// Each square either contains a delivery office or it does not. 
// You may pick a grid square that does not already contain a delivery office and build a new delivery office there.
// The delivery time of a parcel to a square is 0 if that square contains a delivery office. 
// Otherwise, it is defined as the minimum Manhattan distance between that square 
// and any other square containing a delivery office. 
// The overall delivery time is the maximum of delivery times of all the squares. 
// What is the minimum overall delivery time you can obtain by building at most one new delivery office?
// Note: The Manhattan distance between two squares (r1,c1) and (r2,c2) is defined as |r1 - r2| + |c1 - c2|, 
// where |*| operator denotes the absolute value.

// Input
// The first line of the input gives the number of test cases, T. 
// T test cases follow. The first line of each test case contains the number of rows R and number of columns C of the grid. 
// Each of the next R lines contains a string of C characters chosen from the set {0, 1}, 
// where 0 denotes the absence of a delivery office and 1 denotes the presence of a delivery office in the square.

// Output
// For each test case, output one line containing Case #x: y, 
// where x is the test case number (starting from 1) and y is the minimum overall 
// delivery time you can obtain after adding at most one additional delivery office.

// Limits
// Time limit: 15 seconds per test set.
// Memory limit: 1GB.
// 1 ≤ T ≤ 100.
// There is at least one delivery office in the initial grid.

// Test set 1 (Visible)
// 1 ≤ R ≤ 10.
// 1 ≤ C ≤ 10.

// Test set 2 (Hidden)
// 1 ≤ R ≤ 250.
// 1 ≤ C ≤ 250.

// Sample

// Input
// 3
// 3 3
// 101
// 000
// 101
// 1 2
// 11
// 5 5
// 10001
// 00000
// 00000
// 00000
// 10001

// Output 
// Case #1: 1
// Case #2: 0
// Case #3: 2

  
// In Sample Case #1, you get a minimum overall delivery time of 1 by building a new delivery office 
// in any one of the five squares without a delivery office.
// In Sample Case #2, all the squares already have a delivery office and 
// so the minimum overall delivery time is 0. Note you have to add at most one delivery office.
// In Sample Case #3, to get a minimum overall delivery time of 2, 
// you can build a new delivery office in any of these squares: (2, 3), (3, 2), (3, 3), (3, 4), or (4, 3). 
// Any other possibility results in a higher overall delivery time than 2.

#include<iostream>
#include<algorithm>
#include<queue>
#include<limits.h>
#include<cstring>

using namespace std;
const int N = 255;
int n, m;
string g[N];
int dist[N][N];

void bfs(int k){
    queue<pair<int, int>> q;
    memset(dist, -1, sizeof(dist));
    for(int i = 0; i < n; i++)
        for(int j = 0;j < m; j++)
            if(g[i][j] == '1'){
                dist[i][j] = 0;
                q.push({i, j});
            }

    int dx[4] = {-1,0,1,0}, dy[4] = {0,1,0,-1};

    while(q.size()){
        auto t = q.front();
        q.pop();
        int x = t.first, y = t.second;
        int distance = dist[x][y];

        if (distance == k) continue;
        
        for(int i = 0; i < 4; i++){
            int a = x + dx[i], b = y + dy[i];
            if (a >= 0 && a < n && b >= 0 && b < m && dist[a][b] == -1){
                dist[a][b] = distance + 1;
                q.push({a,b});
            }
        }
    }
}

bool check(int k){
    bfs(k);

    int min_sum = INT_MAX, max_sum = INT_MIN;
    int min_sub = INT_MAX, max_sub = INT_MIN;
    for (int i = 0; i < n; i ++ )
        for (int j = 0; j < m; j ++ )
            if (dist[i][j] == -1)
            {
                min_sum = min(min_sum, i + j);
                max_sum = max(max_sum, i + j);
                min_sub = min(min_sub, i - j);
                max_sub = max(max_sub, i - j);
            }

    if (min_sum == INT_MAX) 
        return true;

    for (int i = 0; i < n; i ++ )
        for (int j = 0; j < m; j ++ )
            if (g[i][j] == '0')
            {
                int sum = max(abs(i + j - min_sum), abs(i + j - max_sum));
                int sub = max(abs(i - j - min_sub), abs(i - j - max_sub));
                if (max(sum, sub) <= k) return true;
            }

    return false;
}

int main(){
    int T;
    cin >> T;
    for (int c = 1; c <= T;c++){
        cin >> n >> m;
        for (int i = 0; i < n; i++)
            cin >> g[i];
        
        int l = 0, r = n+m;
        while (l < r){
            int mid = l + r >> 1;
            if (check(mid))
                r = mid;
            else l = mid + 1;
        }
        printf("Case #%d: %d\n",c, r);
    }
    return 0;
}