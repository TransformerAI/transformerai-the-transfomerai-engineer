

import json
from typing import List


class LCTopicTag:
    def __init__(self, name, id, slug):
        name: str = name
        id: str = id
        slug: str = slug
        
    def to_dict(self):
        return {
            "name": self.name,
            "id": self.id,
            "slug": self.slug
        }
        
    @staticmethod
    def from_dict(d: dict) -> 'LCTopicTag':
        return LCTopicTag(
            name=d["name"],
            id=d["id"],
            slug=d["slug"]
        )
        
    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)
    
    @staticmethod
    def from_json(json_str: str) -> 'LCTopicTag':
        return LCTopicTag.from_dict(json.loads(json_str))

class LCProblem:
    def __init__(self, acceptance_rate, difficulty, frequency_bar, frontend_question_id, is_favor, paid_only, status, title, title_slug, topic_tags, has_solution, has_video_solution):
        acceptance_rate: float = acceptance_rate
        difficulty: str = difficulty
        frequency_bar: float = frequency_bar
        frontend_question_id: str = frontend_question_id
        is_favor: bool = is_favor
        paid_only: bool = paid_only
        status: str = status
        title: str = title
        title_slug: str = title_slug
        topic_tags: List[LCTopicTag] = topic_tags
        has_solution: bool = has_solution
        has_video_solution: bool = has_video_solution
        
    def to_dict(self):
        return {
            "acceptance_rate": self.acceptance_rate,
            "difficulty": self.difficulty,
            "frequency_bar": self.frequency_bar,
            "frontend_question_id": self.frontend_question_id,
            "is_favor": self.is_favor,
            "paid_only": self.paid_only,
            "status": self.status,
            "title": self.title,
            "title_slug": self.title_slug,
            "topic_tags": [tag.to_dict() for tag in self.topic_tags],
            "has_solution": self.has_solution,
            "has_video_solution": self.has_video_solution
        }
        
    @staticmethod
    def from_dict(dict) -> 'LCProblem':
        return LCProblem(
            acceptance_rate=dict["acceptance_rate"],
            difficulty=dict["difficulty"],
            frequency_bar=dict["frequency_bar"],
            frontend_question_id=dict["frontend_question_id"],
            is_favor=dict["is_favor"],
            paid_only=dict["paid_only"],
            status=dict["status"],
            title=dict["title"],
            title_slug=dict["title_slug"],
            topic_tags=[LCTopicTag.from_dict(tag) for tag in dict["topic_tags"]],
            has_solution=dict["has_solution"],
            has_video_solution=dict["has_video_solution"]
        )

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)
    
    @staticmethod
    def from_json(json_str: str) -> 'LCProblem':
        return LCProblem.from_dict(json.loads(json_str))