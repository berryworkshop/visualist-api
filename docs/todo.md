1. Basic api
  ✓ `/api/` should load
    ✓ should be json
    ✓ header should have links to `/api/users`, `/api/groups`, `/api/records`

1. Basic e2e
  ✓ `/` should load
    • should have header and footer
    • should be responsive
    • header should have links to `/directory`, `/calendar`, `/map`, `/user`

1. Users
  • `User.generate_key()` should generate new random key, and save at `User.key`
  • should have various levels of permission

1. `/api/users`
  if logged in
    • request should provide token
    • Should provide API access
      • GET, POST at collection
      • GET, POST, PUT, DELETE at item
    • User model should have user key
  else
    • should deny access

1. `/login`
  • should load with form
  • should check credentials against Users upon form submit
  • should return token upon successful credential check
  • should store token in cookie and redirect to url in `next` parameter, else `/`
  • should show flash messages upon login redirect

1. Events
  • `Event.__str__` should provide correct string representation of Event
  • `Event.objects.create()` should work, but only if a User is
    • logged in
    • has permission
  • `Event` owner should be logged-in user

1. `/calendar`
  • should load
  • if logged in, else opposite
    • should find token in request
    • login toggle should be true
    • should provide submit button

1. Event API
  • Should provide API access at `/api/events`
    • GET, POST at collection
    • GET, POST, PUT, DELETE at item
  • GET (item, collection) should work for everybody
  • GET collection should not include non-event records (`Person`, etc.)
  • POST should only work if:
    • User is logged in
    • User has appropriate permissions
  • `/api` should show links to `/api/events`
  • `/api/events` should show links to self, previous, next, parent

1. Model derivative schema
  • Should build JSON schema based on model fields
  • schema should be compatible with Vee-Validate requirements
  • should have basic fields
    • `title`
    • `slug`

1. `/submit`
  if logged in
    • should provide form
    • should have basic fields
      • `title`
      • `slug` (hidden field)
    • form
      • should validate against schema
      • POST submit should work
    • should provide two submit buttons
      • `submit` should redirect to event page
      • `save and submit another` should clear form and not redirect
    • should show flash message upon submit
  otherwise
    • should redirect to `/login`, and put `/submit` into URL params
    • should redirect to `/submit` after successful login

1. other Record types: Person, etc.
  • submission of `Event` should reference any related `Person`
  • `Person` should have same API structure as `Event`
  • `/api/` should show links to `/api/people`
  • `/api/people` should show links to self, previous, next, parent

1. Basic visual system
  • should be responsive

1. Image

1. IIIF

1. Flesh out model fields; test
  • model should contain
  • derivative schema should contain and be accurate

1. Directory
  • should show `Person` and `Organization` records

1. Calendar
  • should show `Event` records

1. Map
  • should show records with related `Place`
