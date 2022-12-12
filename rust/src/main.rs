use rocket::serde::json::{Value, json};

#[macro_use] extern crate rocket;

#[get("/")]
fn index() -> Value {
    let mut counter = 0;
    let counter_max = 100_000;
    while counter < counter_max {
        counter += 1;
    }
    json!({ "hello": "world" })
}

#[launch]
fn rocket() -> _ {
    rocket::build().mount("/", routes![index])
}
