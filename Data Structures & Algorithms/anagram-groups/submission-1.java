class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        for (String word : strs) {
            char[] arrWord = word.toCharArray();
            Arrays.sort(arrWord);
            String sortedWord = new String(arrWord);
            if (map.containsKey(sortedWord)) {
                map.get(sortedWord).add(word);
            } else {
                map.put(sortedWord, new ArrayList<>(List.of(word)));
            }
        }
        return new ArrayList<>(map.values());
    }
}
