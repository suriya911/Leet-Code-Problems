impl Solution {
    pub fn largest_good_integer(num: String) -> String {
        let mut best = String::new();
        let bytes = num.as_bytes();
        for i in 0..bytes.len()-2 {
            if bytes[i] == bytes[i+1] && bytes[i] == bytes[i+2] {
                let cur = &num[i..i+3];
                if cur > &best {
                    best = cur.to_string();
                }
            }
        }
        best
    }
}
