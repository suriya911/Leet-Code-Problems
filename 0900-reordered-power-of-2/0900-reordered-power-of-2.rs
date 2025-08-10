use std::collections::BTreeMap;

impl Solution {
    pub fn reordered_power_of2(n: i32) -> bool {
        fn freq_map(mut n: i32) -> BTreeMap<i32,usize> {
            let mut result = BTreeMap::new();
            while n>0 {
                *result.entry(n%10).or_insert(0) += 1;
                n /= 10;
            }
            result
        }        
        let fq_map = freq_map(n);
        for pow in 0..31 {            
            if fq_map == freq_map(2_i32.pow(pow) as i32) { return true; }
        }        
        false
    }
}