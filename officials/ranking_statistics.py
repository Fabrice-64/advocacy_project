import pandas as pd

class GetStatsFromOfficials:
    def __init__(self, officials):
        self.officials = pd.DataFrame(officials)

    def get_stats_from_officials(self):
        officials_description = self.officials.describe()
        return officials_description.to_dict('dict')

    def get_quantiles_from_officials(self):
        officials_quantiles = self.officials.quantile([0.25, 0.5, 0.75, 1])
        return officials_quantiles.to_dict('dict')

    def get_officials_below_P50_I50(self):
        return self.officials.loc[(
                self.officials['propinquity'] < self.officials['propinquity'].quantile(0.50)) & (
                self.officials['influence'] <self.officials['influence'].quantile(0.50))].to_dict('index')
    
    def get_officials_below_P50_above_I50(self):
        return self.officials.loc[(
                self.officials['propinquity'] < self.officials['propinquity'].quantile(0.50)) & (
                self.officials['influence'] >= self.officials['influence'].quantile(0.50))].to_dict('index')
    
    def get_officials_above_P50_below_I50(self):
        return self.officials.loc[(
                self.officials['propinquity'] >= self.officials['propinquity'].quantile(0.50)) & (
                self.officials['influence'] < self.officials['influence'].quantile(0.50))].to_dict('index')

    def get_officials_above_P50_above_I50(self):
        return self.officials.loc[(
                self.officials['propinquity'] >= self.officials['propinquity'].quantile(0.50)) & (
                self.officials['influence'] >= self.officials['influence'].quantile(0.50))].to_dict('index')

    def get_influence_targets(self):
        return self.officials.loc[(
                self.officials['propinquity'] >= self.officials['propinquity'].quantile(0.40)) & (
                    self.officials['propinquity'] < self.officials['propinquity'].quantile(0.80)) & (
                    self.officials['influence'] >= self.officials['influence'].quantile(0.40))
                    ].to_dict('index')