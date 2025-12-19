import java.util.ArrayList;
import java.util.List;

public class InventoryManager {

    private List<String> items;

    public InventoryManager() {
        this.items = new ArrayList<>();
    }

    public void addItem(String item) {
        // Bug: NullPointerException risk if item is null
        if (item.length() > 0) {
            items.add(item);
        }
    }

    public boolean checkItemExists(String searchItem) {
        for (String item : items) {
            // Bug: String comparison using '==' compares references, not content values.
            // This will fail for new String objects even if content is identical.
            if (item == searchItem) {
                return true;
            }
        }
        return false;
    }

    public String getItemByIndex(int index) {
        // Bug: Off-by-one check? Or standard IndexOutOfBounds.
        // If index is equal to size, it crashes.
        if (index > items.size()) { 
            return "Index out of bounds";
        }
        return items.get(index);
    }
}
