from typing import Optional, Dict, List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Company(BaseModel):
    name: str = None
    title: str = None
    description: Optional[str] = None
    workingTime: Dict[str, str] = None
    address: str = None
    phone: str = None
    geoTag: Optional[str] = None
    instagram: Optional[str] = None
    faceBook: Optional[str] = None
    sections: Dict[str, int] = None


class SubSection(BaseModel):
    subSectionName: str
    id: int


class Section(BaseModel):
    id: int
    sectionName: str
    subsections: List[SubSection]


class Menu(BaseModel):
    company: str
    sections: List[Section]


class Dish(BaseModel):
    dishName: str
    mainImg: str
    sliderImgs: List[str] = []
    subsectionId: int
    description: str
    price: int
    weight: int
    ingredients: List[str] = []
    specialMarks: List[str] = []
    isSpicy: int = 0
    parentSectionId: int


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/{name}")
async def getCompany(name: str):
    company = Company()
    company.name = name
    company.title = "Simple title, base "
    company.workingTime = {"Sunday": "10:00-22:00",
                           "Monday": "10:00-22:00",
                           "Tuesday": "10:00-22:00",
                           "Wednesday": "10:00-22:00",
                           "Thursday": "10:00-22:00",
                           "Friday": "10:00-22:00",
                           "Saturday": "10:00-22:00"}
    company.address = "Radanovici, Черногория"
    company.geoTag = "42.3487998848943, 18.767679742284034"
    company.phone = "+38269877678"
    company.instagram = "www.instagram.com/dfdfs"
    company.sections = {"food": 3, "bar": 5}
    return company


@app.get("/{name}/menu")
async def getCompanyMenu(name: str):
    menu = Menu(company=name, sections=[])
    section = Section(id=3, sectionName="Food", subsections=[])
    section.subsections.append(SubSection(id=3, subSectionName="Main Dish"))
    section.subsections.append(SubSection(id=4, subSectionName="Combo Menu"))
    section.subsections.append(SubSection(id=5, subSectionName="Meet"))
    section.subsections.append(SubSection(id=6, subSectionName="Starters"))

    sectionBar = Section(id=5, sectionName="Bar", subsections=[])
    sectionBar.subsections.append(SubSection(id=1, subSectionName="Cold Soft drinks"))
    sectionBar.subsections.append(SubSection(id=2, subSectionName="Beer"))
    menu.sections.append(section)
    menu.sections.append(sectionBar)

    return menu


@app.get("/{company}/menu/dish/{name}")
async def getDish(name: str):
    dish = Dish(dishName="Meet", mainImg="some-link.jpg", subsectionId=5, description="Text about this dish. What the composition and blah dish. What the and blah blah blah",
                price=345, weight=13,parentSectionId=3)
    return dish
