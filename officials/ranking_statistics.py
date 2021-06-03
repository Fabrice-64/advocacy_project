"""
    This module calculates the ranking of the officials on the basis 
    of the calculations operated in the module calculations.py.
    The data transit from the views :
        def officials_ranking
        def officials_to_engage
    the module calculations computes the data and they 
    are send to this module to sort out the officials.
    
    The named tuples are converted into a pandas DataFrame 
    in order to be processed.

    Two methods are implemented and not used, but may be useful 
    in a further stage:
    get_stats_from_officials:
        returns a pandas description of the dataframe throught the method pd.describe()
    get_quantiles_from_officials:
        returns the quartiles of the dataframe.

    The other methods sort out the officials in different categories, based on quartiles
    get_officials_below_P50_I50:
        officials whose influence and propinquity are below the threshold of 0.5
    get_officials_below_P50_above_I50:
        officials whose propinquity is below the threshold of 0.5, but with a higher influence
    get_officials_above_P50_below_I50:
        officials whose propinquity is above the threshold of 0.5, but with a lower influence
    get_officials_above_P50_above_I50:
        officials who are influential and own a high propinquity with the values of the association.
    
    A method designed to get the influence targets:
    get_influence_targets:
        it loooks for the soft spot: officials who are both rather influential and own a propinquity
        that can grow.

    All these methods returnto the views a list of dictionaries with the relevant officials.

"""
import pandas as pd

class GetStatsFromOfficials:
    def __init__(self, officials):
        """ Create a dataframe to be processed all along the class
            Attribute:
                officials: a list of named tuples
        """
        self.officials = pd.DataFrame(officials)

    def get_stats_from_officials(self):
        officials_description = self.officials.describe()
        return officials_description.to_dict('dict')

    def get_quantiles_from_officials(self):
        officials_quantiles = self.officials.quantile([0.25, 0.5, 0.75, 1])
        return officials_quantiles.to_dict('dict')

    def get_officials_below_P50_I50(self):
        return [value for key, value in self.officials.loc[(
                self.officials['propinquity'] < self.officials['propinquity'].quantile(0.50)) & (
                self.officials['influence'] <self.officials['influence'].quantile(0.50))].to_dict('index').items()]
        
    def get_officials_below_P50_above_I50(self):
        return [value for key, value in self.officials.loc[(
                self.officials['propinquity'] < self.officials['propinquity'].quantile(0.50)) & (
                self.officials['influence'] >= self.officials['influence'].quantile(0.50))].to_dict('index').items()]
    
    def get_officials_above_P50_below_I50(self):
        return [value for key, value in self.officials.loc[(
                self.officials['propinquity'] >= self.officials['propinquity'].quantile(0.50)) & (
                self.officials['influence'] < self.officials['influence'].quantile(0.50))].to_dict('index').items()]

    def get_officials_above_P50_above_I50(self):
        return [value for key, value in self.officials.loc[(
                self.officials['propinquity'] >= self.officials['propinquity'].quantile(0.50)) & (
                self.officials['influence'] >= self.officials['influence'].quantile(0.50))].to_dict('index').items()]

    def get_influence_targets(self):
        return [value for key, value in self.officials.loc[(
                self.officials['propinquity'] >= self.officials['propinquity'].quantile(0.40)) & (
                    self.officials['propinquity'] < self.officials['propinquity'].quantile(0.80)) & (
                    self.officials['influence'] >= self.officials['influence'].quantile(0.40))
                    ].to_dict('index').items()]