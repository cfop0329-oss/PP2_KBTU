CREATE OR REPLACE PROCEDURE upsert_user(n TEXT, p TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = n) THEN
        UPDATE phonebook SET number = p WHERE name = n;
    ELSE
        INSERT INTO phonebook(name, number) VALUES(n, p);
    END IF;
END;
$$;


CREATE PROCEDURE delete_user(n TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook WHERE name = n;
END;
$$;