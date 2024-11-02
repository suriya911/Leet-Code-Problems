class Solution {
  public String predictPartyVictory(String senate) {
    var queue = new ArrayDeque<Character>();

    for (var c : senate.toCharArray())
      queue.offer(c);

    var c = 'R';
    while (!queue.isEmpty()) {
      c = queue.poll();
      queue.offer(c);

      if (c == 'R' && !queue.remove('D'))
        return "Radiant";
      if (c == 'D' && !queue.remove('R'))
        return "Dire";
    }
    return null;
  }
}