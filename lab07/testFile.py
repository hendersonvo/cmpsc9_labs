import pytest
from Tea import Tea
from CustomTea import CustomTea
from SpecialtyTea import SpecialtyTea
from TeaOrder import TeaOrder
from OrderQueue import OrderQueue, QueueEmptyException

# 1. Tests for Tea.py (Base Class)

def test_tea_initialization():
    t = Tea("M")
    assert t.getSize() == "M"
    assert t.getPrice() == 0.0

def test_tea_setters():
    t = Tea("S")
    t.setSize("L")
    t.setPrice(5.50)
    
    assert t.getSize() == "L"
    assert t.getPrice() == 5.50

# 2. Tests for CustomTea.py

def test_custom_tea_initial_prices():
    s_tea = CustomTea("S", "Black")
    m_tea = CustomTea("M", "Green")
    l_tea = CustomTea("L", "Oolong")

    assert s_tea.getPrice() == 10.00
    assert m_tea.getPrice() == 15.00
    assert l_tea.getPrice() == 20.00

def test_custom_tea_flavors_pricing():
    s_tea = CustomTea("S", "White")
    s_tea.addFlavor("Peach")
    s_tea.addFlavor("Mango")
    assert s_tea.getPrice() == 10.50

    m_tea = CustomTea("M", "Black")
    m_tea.addFlavor("Mint")
    assert m_tea.getPrice() == 15.50

    l_tea = CustomTea("L", "Green")
    l_tea.addFlavor("Jasmine")
    assert l_tea.getPrice() == 20.75

def test_custom_tea_methods():
    c = CustomTea("S", "Black")
    assert c.getBase() == "Black"
    
    c.setBase("White")
    assert c.getBase() == "White"

def test_custom_tea_details_string():
    # Case 1: No flavors
    cp1 = CustomTea("S", "Oolong")
    expected_no_flavor = "CUSTOM TEA\nSize: S\nBase: Oolong\nFlavors:\nPrice: $10.00\n"
    assert cp1.getTeaDetails() == expected_no_flavor

    # Case 2: With flavors
    cp1 = CustomTea("L", "Green")
    cp1.addFlavor("peach")
    cp1.addFlavor("jasmine")

    assert cp1.getTeaDetails() == "CUSTOM TEA\nSize: L\nBase: Green\nFlavors:\n\t+ peach\n\t+ jasmine\nPrice: $21.50\n"

# 3. Tests for SpecialtyTea.py

def test_specialty_tea_prices():
    s = SpecialtyTea("S", "Earl Grey")
    m = SpecialtyTea("M", "Matcha")
    l = SpecialtyTea("L", "Chai")

    assert s.getPrice() == 12.00
    assert m.getPrice() == 16.00
    assert l.getPrice() == 20.00

def test_specialty_tea_details_string():
    sp1 = SpecialtyTea("S", "Earl Grey")
    expected = \
"SPECIALTY TEA\n\
Size: S\n\
Name: Earl Grey\n\
Price: $12.00\n"
    assert sp1.getTeaDetails() == expected

# 4. Tests for TeaOrder.py

def test_tea_order_description():
    # Setup objects similar to the prompt example
    ct1 = CustomTea("S", "Black")
    ct1.addFlavor("rose")
    ct1.addFlavor("cardamom") # Price: 10 + 0.25 + 0.25 = 10.50
    
    st1 = SpecialtyTea("M", "Matcha") # Price: 16.00

    order = TeaOrder(400)
    order.addTea(ct1)
    order.addTea(st1)

    expected_output = \
"******\n\
Shipping Distance: 400 miles\n\
CUSTOM TEA\n\
Size: S\n\
Base: Black\n\
Flavors:\n\
\t+ rose\n\
\t+ cardamom\n\
Price: $10.50\n\
\n\
----\n\
SPECIALTY TEA\n\
Size: M\n\
Name: Matcha\n\
Price: $16.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $26.50\n\
******\n"

    assert order.getOrderDescription() == expected_output

def test_tea_order_empty():
    order = TeaOrder(50)
    expected = \
"******\n\
Shipping Distance: 50 miles\n\
TOTAL ORDER PRICE: $0.00\n\
******\n"
    assert "Shipping Distance: 50 miles" in order.getOrderDescription()
    assert "TOTAL ORDER PRICE: $0.00" in order.getOrderDescription()

# 5. Tests for OrderQueue.py (MaxHeap Logic)

def test_order_queue_priority():
    """
    Test that the MaxHeap correctly prioritizes orders with 
    larger shipping distances.
    """
    pq = OrderQueue()
    
    # Create orders with distinct distances
    order_low = TeaOrder(10)
    order_high = TeaOrder(500)
    order_mid = TeaOrder(250)

    # Add a specialty tea to each so they aren't empty (optional but realistic)
    order_low.addTea(SpecialtyTea("S", "A"))
    order_high.addTea(SpecialtyTea("S", "B"))
    order_mid.addTea(SpecialtyTea("S", "C"))

    # Add to queue in mixed order
    pq.addOrder(order_low)
    pq.addOrder(order_high)
    pq.addOrder(order_mid)

    # First pop should be the highest distance (500)
    result1 = pq.processNextOrder()
    assert "Shipping Distance: 500 miles" in result1

    # Second pop should be the next highest (250)
    result2 = pq.processNextOrder()
    assert "Shipping Distance: 250 miles" in result2

    # Third pop should be the lowest (10)
    result3 = pq.processNextOrder()
    assert "Shipping Distance: 10 miles" in result3

def test_order_queue_empty_exception():
    """Test that popping from an empty queue raises QueueEmptyException."""
    pq = OrderQueue()
    
    # Verify the specific exception is raised
    with pytest.raises(QueueEmptyException):
        pq.processNextOrder()

def test_order_queue_duplicate_distances():
    """Test behavior with orders having the same distance."""
    pq = OrderQueue()
    
    order1 = TeaOrder(100)
    order1.addTea(SpecialtyTea("S", "First"))
    
    order2 = TeaOrder(100)
    order2.addTea(SpecialtyTea("S", "Second"))
    
    pq.addOrder(order1)
    pq.addOrder(order2)
    
    # We just want to ensure both come out. 
    # MaxHeap behavior for duplicates depends on implementation,
    # but usually, it's not strictly FIFO for duplicates unless coded specifically.
    res1 = pq.processNextOrder()
    res2 = pq.processNextOrder()
    
    assert "Shipping Distance: 100 miles" in res1
    assert "Shipping Distance: 100 miles" in res2