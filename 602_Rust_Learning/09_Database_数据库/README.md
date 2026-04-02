# 数据库

## 1. SQL数据库

### 使用SQLite
```rust
use rusqlite::{Connection, Result};

struct Person {
    id: i32,
    name: String,
    age: i32,
}

fn main() -> Result<()> {
    let conn = Connection::open("test.db")?;
    
    conn.execute(
        "CREATE TABLE IF NOT EXISTS person (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )",
        [],
    )?;
    
    let person = Person {
        id: 1,
        name: String::from("Alice"),
        age: 30,
    };
    
    conn.execute(
        "INSERT INTO person (id, name, age) VALUES (?1, ?2, ?3)",
        &[&person.id, &person.name, &person.age],
    )?;
    
    let mut stmt = conn.prepare("SELECT id, name, age FROM person")?;
    let person_iter = stmt.query_map([], |row| {
        Ok(Person {
            id: row.get(0)?,
            name: row.get(1)?,
            age: row.get(2)?,
        })
    })?;
    
    for person in person_iter {
        println!("Found person: {:?}", person.unwrap());
    }
    
    Ok(())
}
```

## 2. NoSQL数据库

### 使用Redis
```rust
use redis::{Commands, Connection, RedisError};

fn main() -> Result<(), RedisError> {
    let client = redis::Client::open("redis://127.0.0.1/")?;
    let mut con = client.get_connection()?;
    
    let _: () = con.set("my_key", "my_value")?;
    let value: String = con.get("my_key")?;
    
    println!("Got value from Redis: {}", value);
    
    Ok(())
}
```

## 3. ORM框架

### 使用Diesel
```rust
use diesel::prelude::*;
use diesel::sqlite::SqliteConnection;

#[derive(Queryable)]
struct User {
    id: i32,
    name: String,
    email: String,
}

fn main() {
    let conn = SqliteConnection::establish("database.db").unwrap();
    
    use self::schema::users::dsl::*;
    
    let results = users
        .filter(name.like("%Alice%"))
        .load::<User>(&conn)
        .unwrap();
    
    println!("Found {} users:", results.len());
    for user in results {
        println!("{}: {}", user.id, user.name);
    }
}
```

---

**更新时间：2026-04-01**