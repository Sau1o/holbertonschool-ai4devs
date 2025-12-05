# User Stories: SmartPantry

### User Story 1
As a busy parent, I want to scan grocery barcodes using my phone camera so that I can quickly add items to my digital inventory without manual typing.

**Acceptance Criteria**:
- Camera interface opens within 2 seconds.
- Barcode is recognized and matches product details from the database.
- Item is added to the "Pantry" list with a default expiration date.

**Priority**: MVP

### User Story 2
As a home cook, I want to view a list of recipes based on ingredients I currently have so that I can cook dinner without going to the store.

**Acceptance Criteria**:
- "Suggest Recipes" button queries current inventory.
- Results prioritize recipes where the user has >80% of ingredients.
- Missing ingredients are clearly highlighted in the recipe view.

**Priority**: MVP

### User Story 3
As a budget-conscious shopper, I want to receive push notifications when items are approaching their expiration dates so that I can use them before they spoil to save money.

**Acceptance Criteria**:
- User can set custom alert thresholds (e.g., 2 days before).
- Notification deep-links to recipes using the expiring ingredient.
- User can mark the item as "Consumed" or "Tossed" directly from the alert.

**Priority**: MVP

### User Story 4
As a disorganized shopper, I want to manually adjust stock levels (e.g., "half a bottle of milk") so that I know exactly how much of an item is left without guessing.

**Acceptance Criteria**:
- Detail view of an item allows quantity adjustment (slider or percentage).
- Visual indicator changes color (green to red) as quantity decreases.
- Updates sync instantly to the cloud.

**Priority**: High

### User Story 5
As a user with dietary restrictions, I want to set my profile to filter out allergens (e.g., peanuts, gluten) so that I can ensure all recipe suggestions are safe for me to eat.

**Acceptance Criteria**:
- Profile settings page includes a checklist of common allergens.
- Recipe search results automatically exclude dishes containing selected allergens.
- Warning label appears if a scanned product contains a flagged ingredient.

**Priority**: High

### User Story 6
As a family manager, I want to share my inventory and shopping list with other household members so that I can coordinate shopping and avoid buying duplicate items.

**Acceptance Criteria**:
- User can invite members via email address.
- Changes made by one user (e.g., crossing off a shopping item) reflect on all devices in real-time.
- Activity log shows who added or removed items.

**Priority**: High

### User Story 7
As a planner, I want missing ingredients from a selected recipe to be automatically added to my shopping list so that I don't forget to buy necessary items.

**Acceptance Criteria**:
- "Add to Shopping List" button appears on recipe pages.
- Only items with 0 quantity in inventory are added to the list.
- User can review and uncheck items before finalizing the addition.

**Priority**: High

### User Story 8
As a user who hates typing, I want to add produce items (which have no barcodes) using voice commands so that I can keep my inventory complete with minimal effort.

**Acceptance Criteria**:
- Microphone icon activates voice listening mode.
- System parses "Add 5 apples and 2 pounds of carrots" correctly.
- Items are categorized automatically (e.g., under "Produce").

**Priority**: Medium

### User Story 9
As an eco-conscious user, I want to see a dashboard of my food waste statistics so that I can explicitly track my environmental impact and improve my consumption habits.

**Acceptance Criteria**:
- Dashboard displays monthly "Wasted vs. Consumed" percentage.
- Estimated money lost due to waste is calculated.
- User receives a "Green Badge" for reducing waste month-over-month.

**Priority**: Medium

### User Story 10
As a frequent shopper, I want to upload a photo of my grocery receipt so that I can bulk-add multiple items at once without individual scanning.

**Acceptance Criteria**:
- Image upload parses text via OCR.
- System matches receipt text to database items.
- User is presented with a verification screen to confirm items before final addition.

**Priority**: Medium

### User Story 11
As a curious cook, I want to substitute missing ingredients in a recipe so that I can still cook a meal even if I lack one specific item.

**Acceptance Criteria**:
- "Find Substitute" button appears next to missing ingredients.
- System suggests viable alternatives based on food chemistry/category.
- User can select a substitute to update the recipe instructions.

**Priority**: Low

### User Story 12
As a health-focused user, I want to see the nutritional breakdown of suggested meals so that I can track my calorie and macro-nutrient intake.

**Acceptance Criteria**:
- Recipe view displays calories, protein, carbs, and fat per serving.
- Data is aggregated from the USDA food database.
- Users can sort search results by "Low Calorie" or "High Protein".

**Priority**: Low
