#include <stdio.h>

typedef struct node {
	int max;
	int min;
	int left;
	int right;
} Node;

Node tree[300000];
int arr[100010] = { 0 };

void init_tree(int index, int left, int right);
Node get_max_and_min_node(int index, int start, int end);

int main() {
	int n, m;
	int a, b;

	scanf("%d %d", &n, &m);

	for (int i = 1; i <= n; i++) {
		scanf("%d", &arr[i]);
	}

	init_tree(1, 1, n);

	//	for (int i = 0; i < 8; i++) {
	//		printf("index : %d, left : %d, right : %d, min : %d, max : %d\n", i, tree[i].left, tree[i].right, tree[i].min, tree[i].max);
	//	}

	for (int i = 0; i < m; i++) {
		scanf("%d %d", &a, &b);

		Node node = get_max_and_min_node(1, a, b);
		printf("%d %d\n", node.min, node.max);
	}

	return 0;
}

void init_tree(int index, int left, int right) {
	if (left >= right) {
		tree[index].min = arr[left];
		tree[index].max = arr[left];
		tree[index].right = right;
		tree[index].left = left;
		return;
	}

	init_tree(index * 2, left, (left + right) / 2);
	init_tree(index * 2 + 1, (left + right) / 2 + 1, right);

	int lmin = tree[index * 2].min;
	int lmax = tree[index * 2].max;

	int rmin = tree[index * 2 + 1].min;
	int rmax = tree[index * 2 + 1].max;

	tree[index].right = right;
	tree[index].left = left;
	tree[index].min = lmin < rmin ? lmin : rmin;
	tree[index].max = lmax > rmax ? lmax : rmax;
}

Node get_max_and_min_node(int index, int start, int end) {
	//	printf("search index : %d, start : %d, end : %d\n", index, start, end);
	int right = tree[index].right;
	int left = tree[index].left;

	if (start > right || end < left) {
		Node empty;
		empty.max = -1;
		empty.min = -1;
		return empty;
	}

	if (start <= left && end >= right) {
		return tree[index];
	}

	int middle = (left + right) / 2;

	Node lNode = get_max_and_min_node(index * 2, start, end);
	Node rNode = get_max_and_min_node(index * 2 + 1, start, end);

	if (lNode.min == -1 || lNode.max == -1) {
		return rNode;
	} else if (rNode.min == -1 || rNode.max == -1) {
		return lNode;
	}

	Node node;
	node.min = lNode.min < rNode.min ? lNode.min : rNode.min;
	node.max = lNode.max > rNode.max ? lNode.max : rNode.max;
	return node;
}