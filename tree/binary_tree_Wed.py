# binary_tree.py
#=========================================================================
# 이진 트리를 위한 노드 클래스
# - 연결된 구조로 표현
#============================================================================
# 예시 트리 구조:
#     A
#    / \
#   B   C









#========================================================================
# BTNode 클래스 외부에서 사용할 이진 트리의 연산 함수
# - root: 현재 노드를 나타냄. 보통 트리의 루트(root) 노드부터 시작.
# - root는 이진 트리의 노드 객체이며, .left, .right 속성을 통해 왼쪽과 오른쪽 자식 노드에 접근
#=======================================================================







	
#========================================================================
# 테스트 프로그램 : QUIZ (p.127)
#============================================================================
if __name__ == "__main__":
	# 예시 트리 생성
	#       A
	#      / \
	#     B   C
	#    /   / 
	#   D   E 
	#  / \
	# F  G
	# 링크 표현법으로 이진트리 표현 :
	# 리프 노드 생성
	F = BTNode('F')
	G = BTNode('G')
	E = BTNode('E')
	# 중간 노드 생성
	D = BTNode('D', F, G)
	B = BTNode('B', D)
	C = BTNode('C', E)
	# 루트 노드 생성
	root = BTNode('A', B, C)

	print("노드의 수:", count_nodes(root))
	print("간선의 수:", count_edges(root))
	print("트리의 높이:", tree_height(root))
	print_leaf_nodes(root)
	print("연결되지않은 링크 수:", count_none_links(root))	
	print("배열 표현:", bitree_to_array(root) )
	print("링크 표현:", root)
	print("높이 5인 포화이진트리의 노드 수:", full_binary_tree_nodes(5))
	print("높이 5인 이진트리의 최소 노드 수:", min_nodes_in_binary_tree(5))
	print("높이 5인 이진트리의 최대 노드 수:", max_nodes_in_binary_tree(5))		
#========================================================================
# 테스트 프로그램 : 코드 4.8 p.136
#============================================================================
if __name__ == "__main__":
	# 예시 트리 생성
	#       A
	#      /  \
	#     B     C
	#    / \   / 
	#   D   E  F
	# 링크 표현법으로 이진트리 생성 : 단말 노드 -> 루트
	D = BTNode('D',None, None)
	E = BTNode('E',None, None)
	B = BTNode('B',D, E)
	F = BTNode('F',None, None)
	C = BTNode('C', F, None)
	root = BTNode('A', B, C)

	print("\n전위순회:", end=" ")
	preorder(root)
	print("\n후위순회:", end=" ")
	postorder(root)
	print("\n중위순회:", end=" ")
	inorder(root)
	print("\n레벨순회:", end=" ")
	levelorder(root)
	print()
	print("노드의 개수:", count_nodes(root))
	print("\n트리의 높이:", tree_height(root))
	print("단말 노드의 개수:", count_leaves(root))
	print("간선의 개수:", count_edges(root))

