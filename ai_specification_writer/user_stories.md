# User Stories: SmartPantry

### User Story 1: Rapid Inventory Entry

As a busy parent, I want to scan grocery barcodes using my phone camera so that I can quickly add items to my digital inventory without manual typing.

**Acceptance Criteria**:

* Camera interface opens within 2 seconds.

* Barcode is recognized and matches product details from the database.

* Item is added to the "Pantry" list with a default expiration date.

**Priority**: MVP

### User Story 2: Smart Recipe Suggestions

As a home cook, I want to view a list of recipes based on ingredients I currently have so that I can cook dinner without going to the store.

**Acceptance Criteria**:

* "Suggest Recipes" button queries current inventory.

* Results prioritize recipes where the user has >80% of ingredients.

* Missing ingredients are clearly highlighted in the recipe view.

**Priority**: MVP

### User Story 3: Expiration Alerts

As a budget-conscious shopper, I want to receive push notifications when items are approaching their expiration dates so that I can use them before they spoil to save money.

**Acceptance Criteria**:

* User can set custom alert thresholds (e.g., 2 days before).

* Notification deep-links to recipes using the expiring ingredient.

* User can mark the item as "Consumed" or "Tossed" directly from the alert.

**Priority**: MVP

### User Story 4: Manual Stock Adjustment

As a disorganized shopper, I want to manually adjust stock levels (e.g., "half a bottle of milk") so that I know exactly how much of an item is left without guessing.

**Acceptance Criteria**:

* Detail view of an item allows quantity adjustment (slider or percentage).

* Visual indicator changes color (green to red) as quantity decreases.

* Updates sync instantly to the cloud.

**Priority**: High

### User Story 5: Dietary Restriction Filters

As a user with dietary restrictions, I want to set my profile to filter out allergens (e.g., peanuts, gluten) so that I can ensure all recipe suggestions are safe for me to eat.

**Acceptance Criteria**:

* Profile settings page includes a checklist of common allergens.

* Recipe search results automatically exclude dishes containing selected allergens.

* Warning label appears if a scanned product contains a flagged ingredient.

**Priority**: High

### User Story 6: Household Inventory Sharing

As a family manager, I want to share my inventory and shopping list with other household members so that I can coordinate shopping and avoid buying duplicate items.

**Acceptance Criteria**:

* User can invite members via email address.

* Changes made by one user (e.g., crossing off a shopping item) reflect on all devices in real-time
