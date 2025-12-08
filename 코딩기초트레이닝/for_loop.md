# 값 조건에 따라 다른 값 만들 때 → 삼항 연산자

```python
[값_if_true if 조건 else 값_if_false for 변수 in 반복]
```

- for은 맨 뒤
- 값 선택 / 분기

### Example

```python
[x*2 if x%2==0 else x*3 for x in range(5)]
# 결과: [0, 3, 4, 9, 8]
```

# 필터링

필터 조건 → 특정 값만 포함할 때 → if만 사용

```python
[값 for 변수 in 반복 if 조건]
```

- 값 필터링

### Example

```python
[x for x in range(5) if x%2==0]
# 결과: [0, 2, 4]
```
