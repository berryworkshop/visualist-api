1. Basic visual system
  should be responsive

1. Basic e2e
  `/` should load
    should have header and footer
    should be responsive
    header should have links to `/directory`, `/calendar`, `/map`, `/user`
  `/api` should load
    should show links to `/api/users`

1. User
  Should provide API access at `/api/users`
    GET, POST at collection
    GET, POST, PUT, DELETE at item
  should only work if:
    User is logged in
    User has appropriate permissions
  User model should have user key
  `User.generate_key()` should generate new random key, and save at `User.key`
  should have various levels of permission

1. Login
  `/login` should load with form
  `/login` form submit should check credentials against Users
  should return token upon successful credential check
  should store token in cookie and redirect to url in `next` parameter
  should provide token upon subsequent requests

1. Event
  `Event.__str__` should provide correct string representation of Event
  `Event.objects.create()` should work, but only if a User is
    logged in
    has permission
  `Event` owner should be logged-in user

1. Event API
  Should provide API access at `/api/events`
    GET, POST at collection
    GET, POST, PUT, DELETE at item
  GET (item, collection) should work for everybody
  GET collection should not include non-event records (`Person`, etc.)
  POST should only work if:
    User is logged in
    User has appropriate permissions
  `/api` should show links to `/api/events`
  `/api/events` should show links to self, previous, next, parent

1. Model derivative schema
  Should build JSON schema based on model fields
  schema should be compatible with Vee-Validate requirements

1. Flash Messages
  frontend should show current flash messages

1. Form on frontend for POSTing Events
  if logged in, `/submit` should provide form
  otherwise
    `/submit` should redirect to `/login`, and put `/submit` into URL params
    should redirect to `/submit` after successful login
  form should have basic fields
    `title`
    `slug` (hidden field)
  form should validate against schema
  form POST submit should work
  flash message should indicate success
  should redirect to `/directory`

1. other Record types: Person, etc.
  submission of `Event` should reference any related `Person`
  `Person` should have same API structure as `Event`
  `/api/` should show links to `/api/people`
  `/api/people` should show links to self, previous, next, parent

1. Image

1. IIIF

1. Flesh out model fields; test
  model should contain
  derivative schema should contain and be accurate

1. Directory
  should show `Person` and `Organization` records

1. Calendar
  should show `Event` records

1. Map
  should show records with related `Place`
