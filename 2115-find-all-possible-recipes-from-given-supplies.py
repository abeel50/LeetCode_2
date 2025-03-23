class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        isCooked = {s:True for s in supplies}
        r_idx = {r:i for i,r in enumerate(recipes) }

        def dfs(r):
            if r in isCooked:
                return isCooked[r]
            if r not in recipes:
                return False
            isCooked[r] = False # to handle circular
            for ing in ingredients[r_idx[r]]:
                if not dfs(ing):
                    return False
            isCooked[r] = True
            return isCooked[r]
        
        res = []
        for r in recipes:
            if dfs(r):
                res.append(r)
        return res   
