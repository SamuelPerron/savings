# Accounts
### Models
- Account
    - source → accounts.Source
    - label
    - account_type
    - user → users.User
    - _total_invested_
    - _total_deposits_
    - _available_capital_
    - _roi_
    - _day_pl_
- Source
    - label
- Deposit
    - amount
    - account → accounts.Account
    - date

# Transactions
### Models
- Security
    - ticker
    - exchange → transactions.Exchange
    - _price_
    - _day_pl_
- Position
    - account → accounts.Account
    - security → transactions.Security
    - target_allocation
    - fractional
    - leftovers
    - _current_allocation_
    - _nb_shares_
    - _cost_basis_
    - _total_invested_
    - _current_value_
    - _returns_
- Exchange
    - label
    - name
- Transaction
    - security → transactions.Security
    - account → accounts.Account
    - quantity
    - price
    - side
    - date
    - _cost_

