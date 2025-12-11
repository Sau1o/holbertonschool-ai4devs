-- Generated using Copilot Chat
-- Prompt: "Write a SQL query to join Orders, OrderItems and Products. Calculate total revenue per category for current year. Filter > 1000 revenue."

SELECT 
    p.category,
    SUM(oi.quantity * oi.unit_price) as total_revenue,
    SUM(oi.quantity) as total_items_sold
FROM 
    OrderItems oi
JOIN 
    Orders o ON oi.order_id = o.id
JOIN 
    Products p ON oi.product_id = p.id
WHERE 
    EXTRACT(YEAR FROM o.order_date) = EXTRACT(YEAR FROM CURRENT_DATE)
GROUP BY 
    p.category
HAVING 
    SUM(oi.quantity * oi.unit_price) > 1000
ORDER BY 
    total_revenue DESC;
