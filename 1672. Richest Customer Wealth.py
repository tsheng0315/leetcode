## bf
1. calculate the wealth of each customer
2. find max in the wealth

``` python
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        row=len(accounts)
        col=len(accounts[0])
        output=[]  # output is a list

        for i in range(row):
            ans=0
            for j in range(col):
                ans+=accounts[i][j]
            output.append(ans)  ## append at the end of the list
            
        return max(output)
```

## improved list expression

``` python
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(i) for i in accounts)  # list expression
```

## map function
``` python
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum,accounts)) # map(function, iterable)
```
