class TreeNode<T> {
	constructor(
		public val: T,
		public left: TreeNode<T> | null = null,
		public right: TreeNode<T> | null = null
	) {}
}

class Stack<T> {
	values: T[] = []
	constructor() {}
	append(val: T) {
		this.values.push(val)
	}
	pop(): T | null {
		return this.values.length === 0 ? null : this.values.pop()!
	}
	isEmpty(): boolean {
		return this.values.length === 0
	}
}

const isValidBST = (root: TreeNode<number> | null): boolean => {
	if (!root) {
		return false
	}
	let prev = Number.NEGATIVE_INFINITY
	let stack = new Stack<TreeNode<number>>()
	let curr: TreeNode<number> | null = root
	while (!stack.isEmpty() || curr !== null) {
		if (curr) {
			stack.append(curr)
			curr = curr.left
		} else {
			curr = stack.pop()!
			if (curr.val <= prev) {
				return false
			}
			prev = curr.val
			curr = curr.right
		}
	}
	return true
}

let bTree = new TreeNode(3)
bTree.left = new TreeNode(2)
bTree.right = new TreeNode(5)
console.log(isValidBST(bTree))

let nonValidBst = new TreeNode(3)
nonValidBst.left = new TreeNode(5)
nonValidBst.right = new TreeNode(4)
console.log(isValidBST(nonValidBst))
