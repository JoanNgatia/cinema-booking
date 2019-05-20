### Cinema Seat booking application

- The app displays all the seats in the theater and allow users to book it by clicking it.
- Only one user should be allowed to reserved a specific seat.
- If a seat is available, user is prompted for their name, email address and phone number.On booking, a confirmation email is sent to the user.

#### Setup instructions

#### API reference

| Route         | Resource                         |
| ------------- | -------------------------------  |
| `/seats/`     | View all seats                   |
| `/seats/<id>/`| Select a seat, view availability |
|  `/seats/<id>/book/` | Book a seat               |
