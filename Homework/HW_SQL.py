CREATE TABLE host (
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone_number TEXT,
    address TEXT
);

CREATE TABLE guest (
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone_number TEXT
);

CREATE TABLE room (
    id SERIAL PRIMARY KEY,
    type TEXT NOT NULL,
    price INT NOT NULL,
    capacity INT NOT NULL,
    host_id INT REFERENCES host(id),
    ac BOOLEAN DEFAULT FALSE,
    iron BOOLEAN DEFAULT FALSE,
    balcony BOOLEAN DEFAULT FALSE,
    seaview BOOLEAN DEFAULT FALSE,
    hair_dryer BOOLEAN DEFAULT FALSE,
    wifi BOOLEAN DEFAULT FALSE
);

CREATE TABLE reservation (
    id SERIAL PRIMARY KEY,
    guest_id INT REFERENCES guest(id),
    room_id INT REFERENCES room(id),
    check_in DATE NOT NULL,
    check_out DATE NOT NULL
);

CREATE TABLE review (
    id SERIAL PRIMARY KEY,
    evaluation INT CHECK (evaluation BETWEEN 1 AND 10),
    description TEXT,
    reservation_id INT REFERENCES reservation(id)
);

INSERT INTO host (first_name, last_name, phone_number, address) VALUES 
('John', 'Doe', '123-456-7890', '123 Main St, Anytown, USA'),
('Jane', 'Smith', '234-567-8901', '456 Oak St, Othertown, USA'),
('Emily', 'Johnson', '345-678-9012', '789 Pine St, Sometown, USA');

INSERT INTO guest (first_name, last_name, phone_number) VALUES
('Alice', 'Brown', '456-789-0123'),
('Bob', 'Davis', '567-890-1234'),
('Charlie', 'Miller', '678-901-2345');

INSERT INTO room (type, price, capacity, host_id, ac, iron, balcony, seaview, hair_dryer, wifi) VALUES
('Single', 100, 1, 1, TRUE, FALSE, TRUE, FALSE, TRUE, TRUE),
('Double', 150, 2, 2, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE),
('Suite', 300, 4, 3, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE);

INSERT INTO reservation (guest_id, room_id, check_in, check_out) VALUES
(1, 1, '2024-08-01', '2024-08-05'),
(2, 2, '2024-08-10', '2024-08-15'),
(3, 3, '2024-08-20', '2024-08-25');

INSERT INTO review (evaluation, description, reservation_id) VALUES
(8, 'Great stay, very comfortable.', 1),
(9, 'Excellent service and amenities.', 2),
(7, 'Good experience overall.', 3);

SELECT guest.id, guest.first_name, guest.last_name, COUNT(reservation.id)
FROM guest
JOIN reservation ON guest.id = reservation.guest_id
GROUP BY guest.id, guest.first_name, guest.last_name
ORDER BY COUNT(reservation.id) DESC