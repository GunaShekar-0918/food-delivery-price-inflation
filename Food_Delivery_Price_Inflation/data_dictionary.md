| Column Name             | Data Type            | Meaning                                                          |
| ----------------------- | -------------------- | ---------------------------------------------------------------- |
| restaurant_name         | Text (String)        | Name of the restaurant offering the food item                    |
| food_item               | Text (String)        | Name of the food item sold                                       |
| dine_in_price           | Integer (Number)     | Price of the food item when purchased directly at the restaurant |
| app_price               | Integer (Number)     | Price of the same food item on the delivery app                  |
| discount_shown          | Integer (Percentage) | Discount percentage shown on the delivery app                    |
| delivery_platform       | Text (String)        | Food delivery platform used (Zomato, Swiggy, etc.)               |
| city                    | Text (String)        | City where the restaurant is located                             |
| cuisine_type            | Text (String)        | Type of cuisine (Indian, Italian, Fast Food, etc.)               |
| price_inflation         | Integer (Number)     | Extra amount charged on the app compared to dine-in price        |
| actual_discount_percent | Decimal (Float)      | Actual discount calculated using dine-in and app prices          |
| inflation_flag          | Text (String)        | Indicates whether the app price is inflated or not               |
