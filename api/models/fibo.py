class Fibo:
    def __init__(self, coin_name, entry, take_profit, stop_loss):
        self.coin_name = coin_name
        self.entry = entry
        self.take_profit = take_profit
        self.stop_loss = stop_loss

    def __repr__(self):
        return f'<Fibo {self.coin_name}>'
    
    def to_dict(self):
        return {
            'coin_name': self.coin_name,
            'entry': self.entry,
            'take_profit': self.take_profit,
            'stop_loss': self.stop_loss
        }