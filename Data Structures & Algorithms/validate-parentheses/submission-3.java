class Solution {
    public boolean isValid(String s) {
        ArrayList<Character> stack = new ArrayList<>();
        HashMap<Character, Character> bracketMap = new HashMap<>();
        bracketMap.put('}', '{');
        bracketMap.put(']', '[');
        bracketMap.put(')', '(');

        for (char sym : s.toCharArray()) {
            if (bracketMap.containsKey(sym)) {
                if (!stack.isEmpty() && stack.getLast().equals(bracketMap.get(sym))) {
                    stack.removeLast();
                } else {
                    return false;
                }
            } else {
                stack.add(sym);
            }
        }
        return stack.isEmpty();
    }
}
