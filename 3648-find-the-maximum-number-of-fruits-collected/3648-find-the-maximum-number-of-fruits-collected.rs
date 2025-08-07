impl Solution {
    pub fn max_collected_fruits(fruits: Vec<Vec<i32>>) -> i32 {
        let n = fruits.len();
        let mut total = 0;
        for i in 0..n {
            total += fruits[i][i];
        }

        let mut right_path = vec![0; 3];
        right_path[0] = fruits[0][n - 1];

        let mut bottom_path = vec![0; 3];
        bottom_path[0] = fruits[n - 1][0];

        let mut window = 2;

        for step in 1..(n - 1) {
            let mut new_right = vec![0; window + 2];
            let mut new_bottom = vec![0; window + 2];

            for dist in 0..window {
                let left = if dist >= 1 { right_path[dist - 1] } else { 0 };
                let mid = right_path[dist];
                let right = if dist + 1 < right_path.len() { right_path[dist + 1] } else { 0 };
                new_right[dist] = left.max(mid).max(right) + fruits[step][n - 1 - dist];

                let left = if dist >= 1 { bottom_path[dist - 1] } else { 0 };
                let mid = bottom_path[dist];
                let right = if dist + 1 < bottom_path.len() { bottom_path[dist + 1] } else { 0 };
                new_bottom[dist] = left.max(mid).max(right) + fruits[n - 1 - dist][step];
            }

            right_path = new_right;
            bottom_path = new_bottom;

            if window as i32 - n as i32 + 4 + step as i32 <= 1 {
                window += 1;
            } else if window as i32 - n as i32 + 3 + step as i32 > 1 {
                window -= 1;
            }
        }

        total + right_path[0] + bottom_path[0]
    }
}
