Clean up sensitive data in commits.  Wrapper for BFG Commit Cleaner tool by Roberto Tyley (https://github.com/rtyley).  

## Wrapper for BFG-Cleaner
>
> _"Faster : 10 - 720x faster"_
>
\- About BFG Commit Cleaner tool
- If BFG is 10 - 720x fast, then this script makes it 1000x faster <br>
- Stand-alone: Required JAR file ([bfg-1.13.0.jar](bfg-site)) already included.  

## Instructions
1. `bfg --git [Full Git Repo URL]` Get repo.  Equivalent of `git clone --mirror [Full Repo URL]`
2. `bfg [Original BFG command]` One of the command on original BFG cleaner.  
3. `bfg --add` Apply changes
4. `bfg --push` or `git push`




Roberto Tyley's [Original program](bfg-site)
[bfg-site]: https://rtyley.github.io/bfg-repo-cleaner/
