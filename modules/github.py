from requests import get


class GitHub:
    def __init__(self, repo: str):
        """Get info about GitHub repository"""
        self.repo = repo

    async def get(self):
        try:
            return get(url=f'https://api.github.com/repos/{self.repo}').json()['stargazers_count']
        except KeyError:
            return 'err.'
