import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

import java.util.*;

public class DependencyResolverTest {

    private DependencyResolver resolver;

    @Before
    public void setUp() {
        resolver = new DependencyResolver();
    }

    // Helper to create map quickly
    private Map<String, List<String>> createMap(Object... data) {
        Map<String, List<String>> map = new HashMap<>();
        for (int i = 0; i < data.length; i += 2) {
            String key = (String) data[i];
            String[] values = (String[]) data[i+1];
            map.put(key, Arrays.asList(values));
        }
        return map;
    }

    @Test
    public void test01SimpleChain() {
        Map<String, List<String>> data = createMap("A", new String[]{"B"}, "B", new String[]{"C"}, "C", new String[]{});
        DependencyResolver.ResolutionResult result = resolver.resolve(data);
        assertTrue(result.success);
        assertEquals(Arrays.asList("C", "B", "A"), result.build_order);
    }

    @Test
    public void test02DiamondDependency() {
        Map<String, List<String>> data = createMap(
            "App", new String[]{"Lib1", "Lib2"},
            "Lib1", new String[]{"Core"},
            "Lib2", new String[]{"Core"},
            "Core", new String[]{}
        );
        DependencyResolver.ResolutionResult result = resolver.resolve(data);
        assertTrue(result.success);
        List<String> order = result.build_order;
        assertEquals("Core", order.get(0));
        assertEquals("App", order.get(order.size() - 1));
        assertTrue(order.containsAll(Arrays.asList("Lib1", "Lib2")));
    }

    @Test
    public void test03CircularDependencyDirect() {
        Map<String, List<String>> data = createMap("A", new String[]{"B"}, "B", new String[]{"A"});
        DependencyResolver.ResolutionResult result = resolver.resolve(data);
        assertFalse(result.success);
        assertNotNull(result.error);
    }

    @Test
    public void test04CircularDependencyIndirect() {
        Map<String, List<String>> data = createMap("A", new String[]{"B"}, "B", new String[]{"C"}, "C", new String[]{"A"});
        DependencyResolver.ResolutionResult result = resolver.resolve(data);
        assertFalse(result.success);
    }

    @Test
    public void test05DisconnectedGraphs() {
        Map<String, List<String>> data = createMap(
            "Front", new String[]{"UI"}, "UI", new String[]{},
            "Back", new String[]{"DB"}, "DB", new String[]{}
        );
        DependencyResolver.ResolutionResult result = resolver.resolve(data);
        assertTrue(result.success);
        List<String> order = result.build_order;
        assertTrue(order.indexOf("UI") < order.indexOf("Front"));
        assertTrue(order.indexOf("DB") < order.indexOf("Back"));
    }

    @Test
    public void test06EmptyInput() {
        Map<String, List<String>> data = new HashMap<>();
        DependencyResolver.ResolutionResult result = resolver.resolve(data);
        assertTrue(result.success);
        assertTrue(result.build_order.isEmpty());
    }

    @Test
    public void test07SelfDependency() {
        Map<String, List<String>> data = createMap("A", new String[]{"A"});
        DependencyResolver.ResolutionResult result = resolver.resolve(data);
        assertFalse(result.success);
    }

    @Test
    public void test08RedundantDependencies() {
        Map<String, List<String>> data = createMap("A", new String[]{"B", "B"}, "B", new String[]{});
        DependencyResolver.ResolutionResult result = resolver.resolve(data);
        assertTrue(result.success);
        assertEquals(Arrays.asList("B", "A"), result.build_order);
    }

    @Test
    public void test09ImplicitDependency() {
        Map<String, List<String>> data = createMap("App", new String[]{"Utils"});
        DependencyResolver.ResolutionResult result = resolver.resolve(data);
        assertTrue(result.success);
        assertEquals(Arrays.asList("Utils", "App"), result.build_order);
    }

    @Test
    public void test10ComplexStructure() {
        Map<String, List<String>> data = createMap(
            "Dashboard", new String[]{"Widget", "Auth"},
            "Widget", new String[]{"Charts", "Styles"},
            "Charts", new String[]{"D3"},
            "Auth", new String[]{"Styles", "DB"},
            "Styles", new String[]{}, "DB", new String[]{}, "D3", new String[]{}
        );
        DependencyResolver.ResolutionResult result = resolver.resolve(data);
        assertTrue(result.success);
        List<String> order = result.build_order;
        assertTrue(order.indexOf("D3") < order.indexOf("Charts"));
        assertTrue(order.indexOf("Styles") < order.indexOf("Widget"));
        assertTrue(order.indexOf("Widget") < order.indexOf("Dashboard"));
    }
}
