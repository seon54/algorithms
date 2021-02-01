package programmers.hash;

import java.util.*;


class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map<String, Integer> map = new HashMap<>();

        for (int i = 0; i < participant.length; i++) {
            String name = participant[i];
            if (map.get(name) == null) {
                map.put(name, 1);
            } else {
                Integer v = map.get(name);
                map.put(name, ++v);
            }
        }

        for (int i = 0; i < completion.length; i++) {
            String name = completion[i];
            Integer v = map.get(name);
            map.put(name, --v);
        }

        for (Map.Entry<String, Integer> entry: map.entrySet()) {
            if (entry.getValue() == 1) {
                answer = entry.getKey();
            }
        }
 
        return answer;
    }

    public String solution2(String[] participant, String[] completion) {
        String answer = "";
        Map<String, Integer> map = new HashMap<>();

        for (String name: participant) map.put(name, map.getOrDefault(name, 0) + 1);
        for (String name: completion) map.put(name, map.get(name) - 1);

        for (String name: map.keySet()) {
            if (map.get(name) != 0) {
                answer = name;
                break;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        String[] participant = {"leo", "kiki", "eden"};
        String[] completion = {"eden", "leo"};

        System.out.println(s.solution(participant, completion));
    }
}