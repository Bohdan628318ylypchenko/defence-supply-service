# cold defence crud operations

---

Common requirements:
- ALL REQUEST PARAMETERS SHOULD BE VALIDATED FOR BEING NOT NULL!!!
- Each request comes with user id. For each request, new action should be created, linked with user whose id
  is provided, stored in db. After request completion, action execution_status (success/fail) should be stored.
- Never perform actual record deletion unless required. Instead, set record_status field to FALSE

---

## Supply

---

*POST createSupply*

Creates new supply object

Parameters:
- name: supply name as string
- unit_cost: cost of supply unit as double, **constraints:** > 0 
- unit_type: liter, kilogram, count etc. as string
- norm_unit_count_day: double, represents how many units of supply defence plans to spend for a day, **constraints:** >= 0
- user_id: id of user which initialized operation
- action_description: action comment by user as string

Response:
- 200 (OK) or 201 (CREATED) if success, JSON of created supply
- Any suitable response if failure

---

*GET getSupplyById*

Returns supply object with given id

Parameters:
- supply_id: id of supply to get
- user_id: id of user which initialized operation
- action_description: action comment by user as string

Response:
- 200 (OK), JSON of supply
- Any suitable response if failure

---

*GET getSupplyByName*

Returns supply object with given name

Parameters:
- supply_name: name of supply to get
- user_id: id of user which initialized operation
- action_description: action comment by user as string

Response:
- 200 (OK), JSON of supply
- Any suitable response if failure

---

*DELETE deleteSupplyById*

Deletes supply with given id

Parameters:
- supply_id: id of supply
- user_id: id of user which initialized operation
- action_description: action comment by user as string

Response:
- 200 (OK), JSON of deleted supply
- Any suitable response if failure

---

*DELETE deleteSupplyByName*

Deletes supply with given name

Parameters:
- supply_name: id of supply
- user_id: id of user which initialized operation
- action_description: action comment by user as string

Response:
- 200 (OK), JSON of deleted supply
- Any suitable response if failure

## Availability

---

*POST createAvailability*

Creates availability object

Parameters:
- supply_id: id of supply to create availability for
- unit_count: count of units as double, *constraint:* > 0
- expiration_datetime: expiration datetime of availability
- user_id: id of user which initialized operation
- action_description: action comment by user as string

Response:
- 200 (OK) or 201 (CREATED), JSON of created availability
- Any suitable response if failure

---

*GET getAvailabilityById*

Returns availability with given id

Parameters:
- availability_id: id of availability to get
- user_id: id of user which initialized operation
- action_description: action comment by user as string

Response:
- 200 (OK), JSON of availability
- Any suitable response if failure

---

*GET getAvailabilityListBySupplyId*

Returns all availability records where supply_id equals to given value

Parameters:
- supply_id: supply_id value to find availability with
- user_id: id of user who initialized action
- action_description: action comment by user as string

Response:
- 200 (OK), availability list as JSON
- Any suitable response if failure
(public) supply
---

*DELETE deleteAvailabilityById*

Deletes availability by its id

Parameters:
- availability_id: id of availability to delete
- user_id: id of user which initialized operation
- action_description: action comment by user as string

Response:
- 200 (OK), JSON of deleted availability
- Any suitable response if failure

---

## BUDGET

---

*POST createBudget*

Creates budget object.

Parameters:
- balance: budget's money, *constraint:* > 0
- year: budget's year
- user_id: id of user which initialized operation
- action_description: action comment by user as string
 
Response:
- 200 (OK), JSON of created budget
- Any suitable response if failure

---

*GET getBudgetById*

Returns budget by given id

Parameters:
- budget_id: id of budget to get info of
- user_id: id of user which initialized operation
- action_description: action comment by user as string

Response:
- 200 (OK), JSON of budget
- Any suitable response if failure

---

*GET getBudgetByYear*

Returns budget by given year

Parameters:
- budget_year: year of budget to get info of
- user_id: id of user which initialized operation
- action_description: action comment by user as string

Response:
- 200 (OK), JSON of budget
- Any suitable response if failure

---

*DELETE getBudgetById*

Deletes budget by given id

Parameters:
- budget_id: id of budget to get info of
- user_id: id of user which initialized operation
- action_description: action comment by user as string

Response:
- 200 (OK), JSON of deleted budget
- Any suitable response if failure

---

*DELETE getBudgetByYear*

Deletes budget by given year

Parameters:
- budget_year: year of budget to get info of
- user_id: id of user which initialized operation
- action_description: action comment by user as string

Response:
- 200 (OK), JSON of deleted budget
- Any suitable response if failure
