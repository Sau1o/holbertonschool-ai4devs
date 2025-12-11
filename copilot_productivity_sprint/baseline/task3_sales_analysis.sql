-- Task 3: Analyze e-commerce sales performance by category

SELECT 
    p.category AS Category,
    SUM(oi.quantity * oi.unit_price) AS TotalRevenue,
    SUM(oi.quantity) AS TotalItemsSold
FROM 
    Orders o
JOIN 
    OrderItems oi ON o.id = oi.order_id
JOIN 
    Products p ON oi.product_id = p.id
WHERE 
    -- Assuming PostgreSQL syntax for date extraction, or standard SQL
    EXTRACT(YEAR FROM o.order_date) = EXTRACT(YEAR FROM CURRENT_DATE)
GROUP BY 
    p.category
HAVING 
    SUM(oi.quantity * oi.unit_price) >= 1000
ORDER BY 
    TotalRevenue DESC;
