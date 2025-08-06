class Solution {
public:
    int numOfUnplacedFruits(std::vector<int>& fruits, std::vector<int>& baskets) {
        int result = fruits.size();
        std::vector<int> tree = createTree(baskets.size());

        addArray(tree, baskets);
        calculateTree(tree);

        for (int fruit : fruits) {
            int pos = findLeftmostPos(tree, fruit);
            if (pos != -1) {
                result--;
                removePos(tree, pos);
            }
        }

        return result;
    }

private:
    std::vector<int> createTree(int itemsCount) {
        if (itemsCount == 0) return std::vector<int>();

        int treeSize = 1;
        while (treeSize <= itemsCount / 2) {
            treeSize <<= 1;
        }
        if (treeSize < itemsCount) {
            treeSize <<= 1;
        }
        treeSize = (treeSize << 1) - 1;

        return std::vector<int>(treeSize, 0);
    }

    void addArray(std::vector<int>& tree, const std::vector<int>& arr) {
        int pos = tree.size() / 2;
        for (int item : arr) {
            tree[pos++] = item;
        }
    }

    void calculateTree(std::vector<int>& tree) {
        int n = tree.size();
        for (int i = (n / 2) - 1; i >= 0; i--) {
            int left = tree[(i << 1) + 1];
            int right = tree[(i << 1) + 2];
            tree[i] = std::max(left, right);
        }
    }

    int findLeftmostPos(const std::vector<int>& tree, int val) {
        if (tree[0] < val) {
            return -1;
        }

        int mid = tree.size() / 2;
        int pos = 0;

        while (pos < mid) {
            int leftIdx = (pos << 1) + 1;
            int rightIdx = (pos << 1) + 2;
            if (tree[leftIdx] >= val) {
                pos = leftIdx;
            } else {
                pos = rightIdx;
            }
        }

        return pos;
    }

    void removePos(std::vector<int>& tree, int pos) {
        tree[pos] = 0;

        while (pos > 0) {
            int parent;
            if (pos & 1) {
                parent = pos >> 1;
            } else {
                parent = (pos >> 1) - 1;
            }

            int left = tree[(parent << 1) + 1];
            int right = tree[(parent << 1) + 2];
            int maxVal = std::max(left, right);

            if (tree[parent] != maxVal) {
                tree[parent] = maxVal;
                pos = parent;
            } else {
                break;
            }
        }
    }
};