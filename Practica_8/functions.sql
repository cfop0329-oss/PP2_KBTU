CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(name TEXT, number TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.name, p.number
    FROM phonebook p
    WHERE p.name ILIKE '%' || pattern || '%'
       OR p.number ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_all_contacts()
RETURNS TABLE(name TEXT, number TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT name, number FROM phonebook;
END;
$$ LANGUAGE plpgsql;