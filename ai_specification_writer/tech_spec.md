# Technical Specification: SmartPantry

## System Components
- **Authentication Service**: Manages user registration, login, and secure token generation (JWT). Handles user profiles and dietary preferences.
- **Inventory Management Service**: Handles adding, updating, and removing items from the pantry. Integrates with external Barcode APIs to populate product details automatically.
- **Recipe Matching Engine**: Core logic that compares the user's current inventory against a database of recipes to suggest meals. Handles substitution logic.
- **Notification Service**: Background job runner that checks expiration dates daily and sends push notifications to users via Firebase/APNS.

## Data Models
- **User**
  - `id`: UUID
  - `email`: String
  - `password_hash`: String
  - `dietary_preferences`: Array<String> (e.g., ["vegan", "gluten-free"])
  
- **PantryItem**
  - `id`: UUID
  - `user_id`: UUID (Foreign Key)
  - `product_name`: String
  - `barcode`: String (Optional)
  - `quantity`: Float
  - `expiration_date`: DateTime
  - `status`: Enum (In_Stock, Consumed, Wasted)

- **Recipe**
  - `id`: UUID
  - `title`: String
  - `ingredients`: Array<Object> {name, quantity, unit}
  - `instructions`: Text
  - `tags`: Array<String>

## API Endpoints
- **POST /api/v1/auth/register**
  - Parameters: `email`, `password`, `name`
  - Returns: User object and Access Token.

- **GET /api/v1/inventory/items**
  - Parameters: `user_id`, `sort_by` (optional: 'expiration_date')
  - Returns: List of PantryItem objects.

- **POST /api/v1/inventory/scan**
  - Parameters: `barcode_number`, `image_data` (optional)
  - Returns: Product details (name, category) found from external API.

- **POST /api/v1/recipes/suggest**
  - Parameters: `inventory_ids` (list of item IDs to use), `filters` (dietary)
  - Returns: List of Recipe objects matched by percentage.
