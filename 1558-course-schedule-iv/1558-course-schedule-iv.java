class Solution {
    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        
        //Wah Modiji(Tribute To Modiji For His BirthDay)MODIROCKS!!
        
        ArrayList graph[] = new ArrayList[numCourses];
        List<Boolean>res = new ArrayList<>();
        
        for(int num = 0 ; num<numCourses ; num++){
            graph[num] = new ArrayList<>();
        }
        
        for(int i = 0 ; i<prerequisites.length ; i++){
            for(int j = 0 ; j<prerequisites[0].length ; j++){
                graph[prerequisites[i][0]].add(prerequisites[i][1]);
            }
        }
        
        boolean [][] status = new boolean[numCourses][numCourses];
        for(int i = 0 ; i<numCourses ; i++){
            dfs(i, graph , status , i);
        }
        
        for(int q[]:queries){
            int parent = q[0];
            int child = q[1];
            res.add(status[parent][child]);
        }
        
        return res;
    }
    public void dfs(int node  , ArrayList graph[] , boolean[][]status , int par){
        status[par][node] = true;
        
        for(int i = 0 ; i<graph[node].size() ; i++){
            int child = (int)graph[node].get(i);
            //no repetation
            if(!status[par][child])
                dfs(child, graph , status , par);
        }
    }   
}